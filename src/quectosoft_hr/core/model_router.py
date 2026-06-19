class ModelRouter:
    def route(self, tier, domain=None, privacy_level=None):
        if privacy_level == "strict":
            return "ollama"
        if tier <= 2:
            return "openai"
        if domain in {"bfsi", "healthcare", "govtech"}:
            return "gemini"
        return "ollama"
