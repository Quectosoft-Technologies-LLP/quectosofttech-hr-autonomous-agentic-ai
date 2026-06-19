class ApprovalEngine:
    def required_approver(self, zone):
        return {"low": "autonomous", "medium": "vp", "high": "csuite", "critical": "human"}.get(zone, "vp")
