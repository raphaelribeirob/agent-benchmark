"""Run-result records and aggregate metrics (success, cost, latency, failure taxonomy)."""

from collections import Counter
from dataclasses import dataclass
from enum import StrEnum
from statistics import median


class Condition(StrEnum):
    BASELINE = "no_self_correction"
    SELF_CORRECT = "self_correction"


class Failure(StrEnum):
    # Draft taxonomy - TODO: finalize during spec (after 2026-11-15).
    NONE = "none"
    WRONG_TOOL = "wrong_tool"
    BAD_ARGUMENTS = "bad_arguments"
    LOOP_OR_BUDGET = "loop_or_budget_exceeded"
    WRONG_FINAL_ANSWER = "wrong_final_answer"
    CONSTRAINT_VIOLATION = "constraint_violation"


@dataclass(frozen=True)
class RunResult:
    task_id: str
    condition: Condition
    seed: int
    success: bool
    cost_usd: float
    latency_s: float
    failure: Failure = Failure.NONE


def summarize(results: list[RunResult]) -> dict:
    """Aggregate a list of runs for one condition."""
    if not results:
        raise ValueError("no results")
    return {
        "n": len(results),
        "success_rate": sum(r.success for r in results) / len(results),
        "total_cost_usd": round(sum(r.cost_usd for r in results), 6),
        "median_latency_s": median(r.latency_s for r in results),
        "failures": dict(Counter(r.failure.value for r in results if not r.success)),
    }
