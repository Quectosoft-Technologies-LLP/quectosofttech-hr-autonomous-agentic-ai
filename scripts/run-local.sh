#!/usr/bin/env bash
set -euo pipefail
uvicorn quectosoft_hr.api:app --reload
