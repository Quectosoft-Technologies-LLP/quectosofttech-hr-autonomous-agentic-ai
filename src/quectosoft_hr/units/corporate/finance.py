class FinanceUnit:
    band = "corporate"
    def route(self, objective):
        return {"unit": "finance", "objective": objective, "routed": True}
