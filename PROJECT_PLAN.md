# Project Plan: agent-benchmark

## Domain
Agent reliability and evaluation: tool-using LLM agents in production platforms.

## Target Companies
GitLab (agent foundations), Cohere (agentic platform), Baseten, WRITER. These are roles that
mention agents, tool use or evaluation.

## Evidence
Job descriptions (URLs checked live on 2026-10-22, HTTP 200 with the matching job title):
- GitLab, Backend Engineer (Python), AI Engineering: Agent Foundations: https://job-boards.greenhouse.io/gitlab/jobs/8704363002
- Cohere, Forward Deployed Engineer, Agentic Platform: https://jobs.ashbyhq.com/cohere/b0bcef37-1d20-414f-aade-c54942d63df9
- Baseten, AI Engineer: https://jobs.ashbyhq.com/baseten/b13ec426-d09d-4122-8112-cf25adbd7d60
- WRITER, AI Engineer: https://jobs.ashbyhq.com/writer/40f9e2b4-3284-4a20-b45d-0f5e5dd9108d

Source of the list: `/workspace/career/ai-engineer-pivot-2026-10-22.md`.
TODO: quote the agent and eval requirements from each posting.

Internal context: `/workspace/career/portfolio-roadmap.md` (deliverable, due 2026-12-20).

## Problem
- **User:** an engineer deciding whether to enable self-correction in an agent.
- **Input:** tasks, tools, model, seeds, budgets.
- **Output:** a comparative report: success, cost, latency, failure taxonomy, variance.
- **Failure modes:** non-reproducible runs (model drift, nondeterminism), leaky success checkers,
  cost blow-up from retry loops, task contamination.
- **Success check:** two independent reruns reproduce the headline success rates within a stated
  tolerance. Every failure is classified.

## Selected Project
Benchmark with vs without self-correction on RIVER TEST-based tasks.

# Build Plan
## Timeline
- Spec: after 2026-11-15 (after Eval Lab v1).
- Public v0: by 2026-12-20.

## First Version
One model, one task suite, two conditions, three seeds, a markdown report. It will **not**
include a leaderboard site, multi-model sweeps or the security track.

## Technologies to Demonstrate
- LLM: qwen2.5:7b via local Ollama (official, $0)
- Agents/tools: tool registry, step budget, self-correction loop
- Evaluation: Eval Lab harness, failure taxonomy, reproducibility stats
- Tests: pytest with a deterministic fake model
- Monitoring/logging: per-step traces in `runs/`
- Deployment/demo: public GitHub repo + report (later, no publishing yet)

## Open Decisions
- What exactly RIVER TEST is, and its license.
- Eval Lab repo location.
- Whether and when to merge the AI Security Benchmark.
