# agent-benchmark

![Status: work in progress](https://img.shields.io/badge/status-work%20in%20progress-orange)

> **Status: work in progress.** All results and metrics are TODO; no numbers have been measured yet.

A public, reproducible benchmark of tool-using LLM agents. It compares the same agent **with and
without self-correction** on success, cost, latency and failure types.

> Status: **skeleton**. Spec starts after 2026-11-15; public v0 targeted for 2026-12-20.
> Everything marked TODO is unbuilt. No results are claimed.

## Problem
Self-correction loops (reflect, retry, re-plan) are often added to agents on intuition. They cost
tokens and time, and nobody checks whether they pay off. Teams need a controlled, repeatable
comparison that shows where self-correction helps, where it hurts, and how it fails.

## User
Engineers who build agent features and need to decide whether self-correction is worth enabling
for their workload. Also reviewers evaluating evaluation rigor.

## Input / Output
- **Input:** a task suite (RIVER TEST-based, TBD), an agent config, a model, seeds and budgets.
- **Output:** per-run records and an aggregate report per condition: success rate, cost, latency
  and failure-taxonomy counts, plus variance across seeds.

## Demo
TODO: sample report table and a terminal recording of one run.

## Model
The official model is **qwen2.5:7b, run locally with Ollama** (`ollama pull qwen2.5:7b`), at zero cost.
Cost is reported as token counts, and USD is $0.

## Architecture
Task loader -> agent runner (tool registry, step budget, optional self-correction loop) ->
checker -> `RunResult` records -> aggregator/report. The runner reuses the Eval Lab harness (TODO).
Records and metrics: `src/agent_benchmark/results.py`.

## Tests
`pip install -e ".[dev]" && pytest -q`. Right now there are only smoke tests for the aggregation.
TODO: checker tests, deterministic fake-model end-to-end test.

## Evals
See [evals/README.md](evals/README.md). **TODO: no runs yet.**

## Limitations
- Task source (RIVER TEST) and license not confirmed yet.
- Eval Lab harness not yet linked.
- A single local model (qwen2.5:7b) limits how far the results generalize.
- The security track (prompt injection, tool misuse) is out of scope for v0.

## Agent docs
`AGENTS.md` (agent rules), `SECURITY.md` (security review), `HARNESS.md` (agent-harness evaluation). Gates and templates are adapted from vibe-coding-toolkit (Matheus Gomes, MIT, commit 790a895).
