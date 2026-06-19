# Contributing to Quectosoft HR Agentic AI

**Author & Maintainer:** Subrit Dikshit  
**Email:** subrit@gmail.com · subrit@quectosofttech.com  
**Organisation:** Quectosoft Technologies LLP · Delhi, India

Thank you for contributing. Every issue, discussion, pull request, test, and operational improvement helps strengthen this enterprise agentic AI platform.

---

## Before You Start

- Read the [README](README.md) to understand the architecture and operating model.
- Review existing issues and discussions before starting major work.
- For large features, security-sensitive changes, or new domain verticals, open a discussion first.
- Keep production safety, governance, and auditability in mind for every change.

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/quectosoft-hr-agentic-ai.git
cd quectosoft-hr-agentic-ai

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -e .[dev]
cp .env.example .env

python setup.py
pytest -q
```

If you are working on runtime or deployment paths, also start local dependencies:

```bash
docker compose up -d
```

---

## Ways to Contribute

| Type | What We Need |
|---|---|
| Bug fixes | API, orchestration, RAID, auth, memory, runtime, deployment |
| Agent cards | New YAML cards across governance, SDLC, and domain verticals |
| Domain logic | BFSI, Healthcare, Telecom, Retail, Manufacturing, GovTech |
| Memory backends | Scope-aware improvements, persistence adapters, access control |
| Integrations | Webhooks, enterprise systems, MCP servers, platform tooling |
| DevOps | CI/CD, Kubernetes, Helm, Terraform, observability, backup/restore |
| Security | OIDC, secrets handling, policy gates, auditability, scanning |
| Documentation | Architecture, runbooks, onboarding, deployment and operations |
| Tests | Unit, integration, runtime parity, safety and workflow validation |

---

## Commit Convention

```text
feat(scope): add a new feature
fix(scope): fix a bug
refactor(scope): internal improvement without behavioural change
docs(scope): documentation update
test(scope): add or update tests
chore(scope): tooling, deps, build, or maintenance

Examples:
  feat(agents/healthcare): add healthcare domain review card
  fix(api/auth): reject missing x-api-key on protected routes
  docs(readme): update deployment and runtime sections
  test(orchestration): add DAG approval routing coverage
  chore(ci): add container scan workflow
```

---

## Pull Request Checklist

- [ ] `python setup.py` passes
- [ ] `pytest -q` passes
- [ ] `ruff check src tests` passes
- [ ] `mypy src` passes for changed areas
- [ ] No secrets are hardcoded in code, docs, tests, or manifests
- [ ] `.env.example` updated if new environment variables were introduced
- [ ] README or `docs/` updated for architecture or runtime changes
- [ ] New or changed runtime behaviour includes tests
- [ ] Security-sensitive changes include validation and failure-path coverage
- [ ] New agent cards follow the schema in `config/agents/schema.yaml`
- [ ] New agent cards include `raidconfig`, `memory`, and `workspace` blocks
- [ ] Provider-specific logic stays isolated to integration or LLM layers
- [ ] Production-impacting changes include operational notes where relevant

---

## Code Standards

- Use Python typing consistently.
- Prefer Pydantic models and structured contracts over loose dictionaries where practical.
- Keep JSON outputs deterministic where agents or APIs return structured data.
- Avoid hardcoding agent identity in Python when YAML cards are the intended source of truth.
- Keep business logic, orchestration logic, and integration logic separated.
- Add tests for all meaningful production changes unless there is a clear operational reason not to.

---

## Testing Expectations

At minimum, contributors should run:

```bash
python setup.py
pytest -q
```

For broader changes, also run:

```bash
ruff check src tests
mypy src
```

If your change touches deployment or runtime flows, validate Docker or Kubernetes assets where possible.

---

## Documentation Expectations

Update documentation when you change:
- Public APIs.
- Runtime behaviour.
- Configuration or environment variables.
- Deployment paths.
- Security or governance controls.
- Agent card structure or orchestration design.

---

## Questions?

Open a GitHub Discussion or email: **subrit@quectosofttech.com**