class SecurityUnit:
    band = "corporate"
    def route(self, objective):
        return {"unit": "security", "objective": objective, "routed": True}
