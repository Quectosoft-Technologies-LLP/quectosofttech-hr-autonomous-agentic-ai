class HITLTrigger:
    def trigger(self, zone):
        if zone == "critical": return {"triggered": True, "channel": "slack-email"}
        if zone == "high": return {"triggered": True, "channel": "approval-queue"}
        return {"triggered": False, "channel": None}
