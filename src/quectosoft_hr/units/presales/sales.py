class SalesUnit:
    band = "presales"
    def route(self, objective):
        return {"unit": "sales", "objective": objective, "engaged": True}
