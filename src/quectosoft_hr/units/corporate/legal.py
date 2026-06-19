class LegalUnit:
    band = "corporate"
    def route(self, objective):
        return {"unit": "legal", "objective": objective, "routed": True}
