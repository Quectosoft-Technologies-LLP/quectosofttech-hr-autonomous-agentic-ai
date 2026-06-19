class AdminUnit:
    band = "corporate"
    def route(self, objective):
        return {"unit": "admin", "objective": objective, "routed": True}
