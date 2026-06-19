class ProposalUnit:
    band = "presales"
    def route(self, objective):
        return {"unit": "proposal", "objective": objective, "drafted": True}
