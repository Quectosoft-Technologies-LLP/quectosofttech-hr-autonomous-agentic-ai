#!/usr/bin/env bash
set -euo pipefail
cp .env.example .env
pip install -e .[dev]
