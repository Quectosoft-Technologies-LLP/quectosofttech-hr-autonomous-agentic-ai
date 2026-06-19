#!/usr/bin/env bash
set -euo pipefail
SQL_FILE=${1:?sql file required}
psql "$DATABASE_URL" < "$SQL_FILE"
