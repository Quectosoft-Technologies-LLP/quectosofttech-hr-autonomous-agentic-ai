#!/usr/bin/env python3
import ast
from pathlib import Path

BASE = Path(__file__).parent
REQUIRED = [
    'pyproject.toml', 'README.md', '.env.example', 'Dockerfile', 'docker-compose.yml',
    '.github/workflows/ci.yml', '.github/workflows/codeql.yml', '.github/dependabot.yml',
    'alembic.ini', 'src/quectosoft_hr/api.py', 'src/quectosoft_hr/core/project_manager.py',
    'src/quectosoft_hr/core/live_events.py', 'src/quectosoft_hr/orchestration/openclaw/templates.py',
    'tests/test_phase3_runtime.py'
]

def verify_required():
    missing = [p for p in REQUIRED if not (BASE / p).exists()]
    if missing:
        raise SystemExit(f'Missing required files: {missing}')

def verify_syntax():
    count = 0
    for pyf in sorted(BASE.rglob('*.py')):
        if 'output' in pyf.parts:
            continue
        ast.parse(pyf.read_text(encoding='utf-8'))
        count += 1
    return count

if __name__ == '__main__':
    verify_required()
    count = verify_syntax()
    print(f'Verified {count} Python files.')
