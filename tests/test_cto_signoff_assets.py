from pathlib import Path

REQUIRED = [
    'deploy/k8s/external-secret.yaml',
    'deploy/k8s/certificate.yaml',
    'config/security/oidc.yaml',
    'scripts/backup.sh',
    'scripts/restore.sh',
    'loadtests/k6/project_api.js',
    '.github/workflows/supply-chain.yml',
    '.github/workflows/container-scan.yml',
    'helm/quectosoft-hr/Chart.yaml',
    'terraform/main.tf',
    'deploy/k8s/overlays/staging/kustomization.yaml',
    'deploy/k8s/overlays/production/kustomization.yaml',
    'deploy/monitoring/prometheus-rule.yaml',
    'deploy/monitoring/grafana-dashboard.json',
]

def test_cto_signoff_assets_present():
    for rel in REQUIRED:
        assert Path(rel).exists(), rel
