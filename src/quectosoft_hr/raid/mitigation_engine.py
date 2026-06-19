class MitigationEngine:
    def recommend(self, zone):
        return {"low": ["continue autonomously and log rationale"], "medium": ["request VP review", "add contingency task"], "high": ["pause pipeline", "request C-suite approval"], "critical": ["stop execution", "trigger human review immediately"]}.get(zone, ["review manually"])
