from pathlib import Path
import yaml
class PolicyEnforcer:
    def __init__(self, policy_path="config/org/corporate_policies.yaml"):
        self.policies = yaml.safe_load(Path(policy_path).read_text(encoding="utf-8")).get("policies", {})
    def validate(self, payload):
        violations = []
        if self.policies.get("human_override_required_for_critical") and payload.get("raid_zone") == "critical" and not payload.get("human_approved"):
            violations.append("critical actions require human approval")
        if self.policies.get("data_protection") == "strict" and payload.get("public_data_dump"):
            violations.append("public data dump is blocked by policy")
        return {"allowed": not violations, "violations": violations}
