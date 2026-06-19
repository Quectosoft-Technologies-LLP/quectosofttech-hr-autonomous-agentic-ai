#!/usr/bin/env bash
set -euo pipefail
python setup.py
pytest -q
