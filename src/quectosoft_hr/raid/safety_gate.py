from quectosoft_hr.raid.threshold_evaluator import ThresholdEvaluator
class SafetyGate:
    def __init__(self):
        self.thresholds = ThresholdEvaluator()
    def review(self, score):
        zone = self.thresholds.zone(score)
        return {"score": score, "zone": zone, "blocked": zone in {"high", "critical"}}
