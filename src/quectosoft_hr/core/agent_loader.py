from pathlib import Path
import yaml
REQUIRED_KEYS = {"id", "name", "tier", "department", "role", "model", "responsibilities", "tools", "raidconfig", "memory", "workspace"}
class AgentLoader:
    def __init__(self, root="config/agents/catalog"):
        self.root = Path(root)
    def load_cards(self):
        cards = []
        for path in sorted(self.root.rglob("*.yaml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            missing = REQUIRED_KEYS - set(data or {})
            if missing:
                raise ValueError(f"Invalid card {path}: missing {sorted(missing)}")
            cards.append(data)
        return cards
