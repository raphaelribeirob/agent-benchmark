from agent_benchmark import __version__
from agent_benchmark.results import Condition, Failure, RunResult, summarize


def test_package_imports():
    assert __version__


def test_summarize_toy_runs():
    runs = [
        RunResult("t1", Condition.BASELINE, 1, True, 0.0, 1.0),
        RunResult("t2", Condition.BASELINE, 1, False, 0.0, 3.0, Failure.WRONG_TOOL),
    ]
    s = summarize(runs)
    assert s["n"] == 2
    assert s["success_rate"] == 0.5
    assert s["median_latency_s"] == 2.0
    assert s["failures"] == {"wrong_tool": 1}
