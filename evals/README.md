# Evals

Status: **TODO. The spec starts after 2026-11-15. No runs, no numbers.**

## Design (draft)
- **Conditions:** the same agent, model and tools, with self-correction turned off and on
  (self-correction means reflecting on tool errors or failed checks and retrying within a budget).
- **Tasks:** derived from RIVER TEST (TBD: confirm the source and license with Raphael).
- **Metrics per condition:** success rate, cost (tokens, then USD), latency (median / p95),
  failure taxonomy counts (`src/agent_benchmark/results.py`), and reproducibility (variance across
  seeds and repeats, with pinned model and harness versions).
- **Model:** qwen2.5:7b via local Ollama (zero cost).
- **Harness:** reuse the Eval Lab runner (TODO: link the repo once it is published).
- **Later:** possibly merge an AI Security track (prompt injection, tool misuse).

Config placeholder: `evals/config.yaml`.
