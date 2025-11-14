from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Azure OpenAI
    azure_openai_api_key: str
    azure_openai_endpoint: str
    azure_openai_model: str = "gpt-4.1-mini"
    azure_openai_api_version: str = "2024-09-01-preview"

    # Agent
    agent_max_steps: int = 10
    agent_debug: bool = False

    # FastAPI server
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    # PostgreSQL (shared between session store + tooling)
    server_host: str = "digiedu-db"
    server_port: int = 5432
    server_db: str = "develop"
    server_user: str = "testuser"
    server_password: str = "pleaseletmein"

    class Config:
        env_file = ".env"
        env_prefix = ""
        case_sensitive = False


settings = Settings()
