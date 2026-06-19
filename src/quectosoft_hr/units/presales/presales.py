class PresalesUnit:
    band = "presales"
    def route(self, objective):
        return {"unit": "presales", "objective": objective, "qualified": True}
