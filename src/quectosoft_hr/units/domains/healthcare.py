class HealthcareUnit:
    band = "domains"
    def review(self, objective):
        return {"unit": "healthcare", "objective": objective, "reviewed": True}
