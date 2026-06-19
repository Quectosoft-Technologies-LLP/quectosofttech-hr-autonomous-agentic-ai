class ReleaseUnit:
    band = "sdlc"
    def route(self, objective):
        return {"unit": "release", "objective": objective, "routed": True}
