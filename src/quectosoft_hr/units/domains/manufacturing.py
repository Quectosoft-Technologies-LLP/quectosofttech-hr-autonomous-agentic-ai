class ManufacturingUnit:
    band = "domains"
    def review(self, objective):
        return {"unit": "manufacturing", "objective": objective, "reviewed": True}
