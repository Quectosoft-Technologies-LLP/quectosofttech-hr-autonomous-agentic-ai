# Quectosoft HR Agentic AI Enterprise

[![CI](https://github.com/quectosofttech/quectosoft-hr-agentic-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/quectosofttech/quectosoft-hr-agentic-ai/actions/workflows/ci.yml)
[![CodeQL](https://github.com/quectosofttech/quectosoft-hr-agentic-ai/actions/workflows/codeql.yml/badge.svg)](https://github.com/quectosofttech/quectosoft-hr-agentic-ai/actions/workflows/codeql.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-QSAL--1.0-01696f.svg)](LICENSE)

Enterprise-grade autonomous Agentic AI platform for HR operations, governance orchestration, domain-aware reviews, RAID control, and production-focused runtime delivery.

## Overview

Quectosoft HR Agentic AI is a multi-agent enterprise platform designed to coordinate HR, governance, delivery, compliance, and domain-specific workflows through structured agent cards, orchestrated execution, memory scopes, approval gates, and deployment-ready runtime assets.

The repository is built for:
- Enterprise HR workflow orchestration.
- Multi-layer governance with human approval for high-risk actions.
- Domain-aware project planning across BFSI, Healthcare, Telecom, Retail, Manufacturing, and GovTech.
- GitHub-ready delivery with CI, security workflows, supply-chain controls, and deployment assets.

## Key Features

- Dynamic YAML-based agent catalog across board, C-suite, VP, corporate, SDLC, pre-sales, sales, and domain verticals.
- OpenClaw-style DAG planning with dependency ordering, approval routing, and HITL checkpoints.
- RAID scoring, thresholding, mitigation recommendations, and escalation triggers.
- Multi-scope memory model for agent, team, department, project, and organisation contexts.
- FastAPI runtime for health, catalog, RAID, and project planning APIs.
- Live project event streaming over WebSocket.
- Enterprise packaging with Docker, Kubernetes, Helm, Terraform, observability, and GitHub workflows.
- CTO-signoff assets for secrets management, TLS, OIDC, backup/restore, DR, load testing, SBOM/signing, and scanning.

## Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    API Layer (FastAPI)                     │
│   Health -  Catalog -  RAID -  Projects -  WebSocket Stream   │
└─────────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────────────────────────────────────────┐
│                  Orchestration & Governance                │
│   OpenClaw DAG -  Approval Engine -  HITL -  Policy Gates    │
└─────────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────────────────────────────────────────┐
│                     Agent Catalog Layer                    │
│  Board -  C-Suite -  VP -  Corporate -  SDLC -  Domains        │
└─────────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────────────────────────────────────────┐
│                  Memory & Runtime Services                 │
│  Agent -  Team -  Department -  Project -  Organisation       │
└─────────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────────────────────────────────────────┐
│                Delivery & Production Assets                │
│ Docker -  K8s -  Helm -  Terraform -  CI -  CodeQL -  Trivy     │
└─────────────────────────────────────────────────────────────┘
```

## Repository Structure

```text
quectosoft-hr-agentic-ai/
├── src/
│   └── quectosoft_hr/
│       ├── agents/
│       ├── core/
│       ├── orchestration/
│       ├── raid/
│       ├── memory/
│       ├── integrations/
│       ├── mcp/
│       ├── units/
│       ├── tools/
│       ├── config/
│       ├── api.py
│       └── worker.py
├── config/
│   ├── agents/
│   ├── access_control/
│   ├── memory/
│   ├── mcp/
│   ├── org/
│   ├── runtime/
│   └── security/
├── deploy/
│   ├── k8s/
│   └── monitoring/
├── helm/
├── terraform/
├── loadtests/
├── docs/
├── tests/
├── .github/workflows/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Quick Start

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Git
- Kubernetes cluster for production deployment
- Optional LLM/API credentials depending on provider strategy

### Local Setup

```bash
git clone https://github.com/quectosofttech/quectosoft-hr-agentic-ai.git
cd quectosoft-hr-agentic-ai

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -e .[dev]
cp .env.example .env

python setup.py
pytest -q
```

### Run Locally

```bash
uvicorn quectosoft_hr.api:app --host 0.0.0.0 --port 8000 --reload
```

### Run with Docker

```bash
docker compose up -d
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/v1/health` | Service health check |
| GET | `/v1/catalog` | Agent catalog summary |
| GET | `/v1/raid` | RAID summary and recent entries |
| POST | `/v1/projects` | Create a new project plan |
| GET | `/v1/projects/{project_id}` | Retrieve a generated project |
| WS | `/v1/projects/{project_id}/stream` | Live event stream for project updates |

### Example Request

```bash
curl -X POST http://localhost:8000/v1/projects \
  -H "Content-Type: application/json" \
  -H "x-api-key: change-me-admin-key" \
  -d '{
    "client_id": "acme",
    "objective": "Launch healthcare onboarding platform",
    "budget": 50000,
    "timeline_days": 45,
    "domain": "healthcare",
    "privacy_level": "strict"
  }'
```

## Configuration

Environment-driven configuration is supported through `.env.example`.

Common settings include:
- Runtime environment and logging.
- API authentication keys.
- LLM primary and fallback provider routing.
- Redis, PostgreSQL, and Chroma persistence.
- Worker and API runtime settings.

## Deployment

### Docker Compose

```bash
docker compose up -d
```

### Kubernetes

```bash
kubectl apply -f deploy/k8s/
```

### Helm

```bash
helm install quectosoft-hr ./helm/quectosoft-hr
```

### Terraform

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

## Production Controls

This repository includes production-oriented assets for:
- External secrets integration.
- TLS ingress and certificate management.
- OIDC/SSO configuration.
- Backup and restore scripting.
- Disaster recovery documentation.
- k6 performance testing.
- SBOM and signing workflow placeholders.
- Container vulnerability scanning.
- Prometheus alerting and Grafana dashboard scaffolds.

## Development

```bash
make install
make lint
make typecheck
make test
make verify
```

If `make` is not available:

```bash
pip install -e .[dev]
ruff check src tests
mypy src
pytest -q
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Code of Conduct

This project follows the community standards in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

This repository is licensed under the Quectosoft Technologies LLP Agentic AI License (QSAL-1.0). See [LICENSE](LICENSE).

## Contact

- Author: Subrit Dikshit
- Work: subrit@quectosofttech.com
- Personal: subrit@gmail.com
- Organisation: Quectosoft Technologies LLP, Delhi, India
- GitHub: https://github.com/quectosofttech
