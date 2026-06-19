import json
class LLMTool:
    def __init__(self):
        self.settings = None
    def provider_sequence(self, primary="ollama", fallbacks=None):
        fallbacks = fallbacks or ["openai", "gemini", "grok"]
        result = []
        for item in [primary] + list(fallbacks):
            if item not in result:
                result.append(item)
        return result
    async def generate(self, prompt, system="You are a helpful assistant."):
        return {"provider": "stub", "raw_response": prompt, "system": system}
    def coerce_json(self, raw, provider):
        text = raw.strip()
        try:
            parsed = json.loads(text)
            if isinstance(parsed, dict):
                parsed.setdefault("provider", provider)
                return parsed
        except json.JSONDecodeError:
            pass
        return {"provider": provider, "raw_response": raw}
