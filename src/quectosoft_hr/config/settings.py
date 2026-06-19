from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ENV: str = 'production'
    LOGLEVEL: str = 'INFO'
    DATABASE_URL: str = 'sqlite:///./quectosoft_hr.db'
    REDIS_URL: str = 'redis://localhost:6379/0'
    CELERY_BROKER: str = 'redis://localhost:6379/1'
    AUTH_API_KEYS: str = 'local-dev-key'
    WEBHOOK_SECRET: str = ''
    LLM_PROVIDER: str = 'ollama'
    LLM_FALLBACKS: str = 'openai,gemini,grok'
    LLM_TEMPERATURE: float = 0.2
    LLM_MAX_TOKENS: int = 2048
    OLLAMA_HOST: str = 'http://localhost:11434'
    OLLAMA_MODEL: str = 'llama3.1:8b'
    OPENAI_API_KEY: str = ''
    OPENAI_BASE_URL: str = 'https://api.openai.com/v1'
    OPENAI_MODEL: str = 'gpt-4o-mini'
    GROK_API_KEY: str = ''
    GROK_BASE_URL: str = 'https://api.x.ai/v1'
    GROK_MODEL: str = 'grok-2-latest'
    GEMINI_API_KEY: str = ''
    GEMINI_BASE_URL: str = 'https://generativelanguage.googleapis.com/v1beta'
    GEMINI_MODEL: str = 'gemini-1.5-pro'
    CHROMA_PERSIST: str = '.chromadb'
    API_HOST: str = '0.0.0.0'
    API_PORT: int = 8000
    WORKERS: int = 4
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    @property
    def api_keys(self):
        return [x.strip() for x in self.AUTH_API_KEYS.split(',') if x.strip()]

    @property
    def fallback_providers(self):
        return [x.strip().lower() for x in self.LLM_FALLBACKS.split(',') if x.strip()]

@lru_cache
def get_settings():
    return Settings()
