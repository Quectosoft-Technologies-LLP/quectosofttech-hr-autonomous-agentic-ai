from pathlib import Path
import yaml
class AccessController:
    def __init__(self, config_path="config/access_control/rbac_matrix.yaml"):
        self.config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    def can(self, role_band, action):
        return action in self.config.get("roles", {}).get(role_band, [])
class AccessLogger:
    def __init__(self):
        self.events = []
    def log(self, actor, scope, action):
        self.events.append({"actor": actor, "scope": scope, "action": action})
