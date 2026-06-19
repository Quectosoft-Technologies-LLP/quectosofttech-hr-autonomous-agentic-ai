class ThresholdEvaluator:
    def zone(self, score):
        if score <= 6: return "low"
        if score <= 12: return "medium"
        if score <= 19: return "high"
        return "critical"
