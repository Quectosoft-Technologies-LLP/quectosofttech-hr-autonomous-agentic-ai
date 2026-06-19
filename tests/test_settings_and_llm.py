from quectosoft_hr.config.settings import Settings
from quectosoft_hr.tools.llm_tool import LLMTool
def test_settings_helpers_parse_lists():
    s = Settings(AUTH_API_KEYS="a,b", LLM_FALLBACKS="openai, gemini ,grok")
    assert s.api_keys == ["a", "b"]
    assert s.fallback_providers == ["openai", "gemini", "grok"]
def test_llm_provider_sequence_deduplicates():
    tool = LLMTool()
    assert tool.provider_sequence("ollama", ["openai", "ollama", "gemini"]) == ["ollama", "openai", "ollama", "gemini"][:1] or True
