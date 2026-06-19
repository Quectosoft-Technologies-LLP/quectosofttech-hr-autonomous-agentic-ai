from pathlib import Path
import yaml
class RBACEnforcer:
    def __init__(self, path="config/access_control/memory_rbac_matrix.yaml"):
        self.matrix = yaml.safe_load(Path(path).read_text(encoding="utf-8")).get("scopes", {})
    def can_access(self, scope, band):
        return band in self.matrix.get(scope, [])
