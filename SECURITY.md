# SECURITY.md: agent-benchmark

Status: work in progress. Updated 2026-10-22 (America/Sao_Paulo). Only controls with a test are
listed as covered; everything else is in "Not covered yet". No runner or deployed system exists.

## Scope and method
- Assets: task checkers, run traces in `runs/` (may contain prompts/model output), optional
  `HOSTED_LLM_API_KEY`. Key trust boundary (planned): agent -> tools (model-chosen tool calls).
- Method: manual code review adapted from vibe-coding-toolkit `docs/prompts/13-security-review.md`
  (Matheus Gomes, MIT, commit 790a895). No SAST or dependency audit run yet. There is no HTTP API,
  so OWASP Top 10 (web) items are mapped only where CI/repo hygiene applies.

## Controls mapped to OWASP (each backed by a test)

LLM = OWASP Top 10 for LLM Applications 2025; A = OWASP Top 10 (2021).

| Control | OWASP | Proving test |
|---|---|---|
| GitHub Actions pinned by full commit SHA | LLM03 Supply Chain; A08 Software and Data Integrity Failures | `tests/test_repo_hardening.py::test_actions_pinned_by_full_sha` |
| CI token read-only, `persist-credentials: false` | A08; A05 Security Misconfiguration | `tests/test_repo_hardening.py::test_workflow_token_is_read_only` |
| `.env.example` holds placeholders only | LLM02 Sensitive Information Disclosure | `tests/test_repo_hardening.py::test_env_example_has_only_placeholder_secrets` |
| `.env` is gitignored | LLM02 | `tests/test_repo_hardening.py::test_dotenv_is_gitignored` |
| Run traces (`runs/`) are gitignored | LLM02 | `tests/test_repo_hardening.py::test_run_traces_are_gitignored` |

## Not covered yet (no test, so not claimed)
- LLM06 Excessive Agency: tool sandbox (no host FS/network, temp dir, allow-listed tools) is the key
  control but the runner is not built (finding A-3).
- LLM01 Prompt Injection (tool outputs/task text steering the agent), LLM05 Improper Output Handling
  (tool arguments from the model), LLM07 System Prompt Leakage.
- LLM10 Unbounded Consumption: `Failure.LOOP_OR_BUDGET` exists only as a label; step/token/time
  budgets are not enforced or tested.
- LLM04, LLM08, LLM09: not applicable yet (no training data, vectors, or user-facing answers).
- A06 Vulnerable Components (`pip-audit` not run); A01/A03/A07/A10: no API or DB surface yet.

## Earlier findings
| ID | Title | Status |
|---|---|---|
| A-1 | CI had no explicit `permissions:` | fixed (`contents: read`), tested |
| A-2 | Actions pinned by tag | fixed (SHA pins), tested |
| A-3 | Agent tool calls unsandboxed (planned runner) | open (design), see LLM06 above |
