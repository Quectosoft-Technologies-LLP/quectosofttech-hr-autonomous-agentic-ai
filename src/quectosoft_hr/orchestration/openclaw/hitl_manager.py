class HITLManager:
    def should_pause(self, zone):
        return zone in {"high", "critical"}
    def channel(self, zone):
        return "slack-email" if zone == "critical" else "approval-queue"
