# SECURITY.md: agent-benchmark

## Scope
- Date: 2026-10-22 (America/Sao_Paulo). Mode: repository baseline of the local checkout plus the
  changes in this commit. Single local repository with no remote. Git history is 2-3 commits.
- Authorization assumed: inspection of this local repo only. No deployed system exists.
- Assets (planned): task checkers, run traces in `runs/` (gitignored). Trust boundaries (planned): agent to tools. Agents under test run model-chosen tool calls, so the tool sandbox is the key control.

## Method
Repository-mode baseline review adapted from vibe-coding-toolkit `docs/prompts/13-security-review.md`
(Matheus Gomes, MIT, commit 790a895). The review was done by manual code tracing and focused
searches. No dedicated security skills or analyzers were installed or used. Note: the prompt
recommends a private report outside the repository. The owner explicitly asked for `SECURITY.md`
in the repo, so this file contains redacted content only.

## Coverage
- Reviewed: all tracked files (`src/`, `tests/`, `evals/`, `data/`, `.github/`, `pyproject.toml`,
  `.env.example`, `.gitignore`).
- Searches: hard-coded secrets (none found; `.env.example` holds empty or placeholder values only),
  shell/eval/deserialization sinks (none in `src/`), and CI triggers and permissions.
- Not run: dependency audit (the project declares no runtime dependencies yet), SAST tools,
  dynamic tests. There is no deployed target.

## Findings

| ID | Title | Severity | Status | Fix |
|---|---|---|---|---|
| A-1 | CI workflow had no explicit `permissions:` block, so `GITHUB_TOKEN` scope depended on repo/org defaults | low (hardening) | confirmed (static) | **fixed**: `permissions: contents: read`, `persist-credentials: false` |
| A-2 | Third-party actions pinned by tag (`@v4`, `@v5`) rather than commit SHA | low (hardening) | confirmed (static) | **fixed 2026-10-22**: pinned to full commit SHAs with `# vX` comments, resolved via `git ls-remote` of the tag and checked against GitHub |
| A-3 | Planned: agents under test execute model-chosen tool calls; without a sandbox a tool could touch the host FS/network | medium (design) | hypothesis, runner not built | proposed: tools are pure-Python fakes or run in a no-network container with a temp dir; add tests that deny out-of-scope paths |

No critical, high or medium findings were substantiated in the inspected scope. That does not mean
the project is secure. Most of the attack surface is not built yet.

## Residual risk and next validation
- Re-review when the runner and tools exist, especially before merging the AI Security track
  (prompt injection, tool misuse), which deliberately adds hostile inputs.
