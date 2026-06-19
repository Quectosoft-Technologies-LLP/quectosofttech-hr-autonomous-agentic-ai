class InfraUnit:
    band = "corporate"
    def route(self, objective):
        return {"unit": "infra", "objective": objective, "routed": True}
