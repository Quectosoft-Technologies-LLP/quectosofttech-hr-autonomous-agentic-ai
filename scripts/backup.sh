#!/usr/bin/env bash
set -euo pipefail
STAMP=$(date +%Y%m%d%H%M%S)
mkdir -p backups
pg_dump "$DATABASE_URL" > "backups/postgres-${STAMP}.sql"
tar -czf "backups/chroma-${STAMP}.tgz" .chromadb || true
