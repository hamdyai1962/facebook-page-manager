from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "facebook-page-manager"
    app_env: str = "development"
    app_debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    meta_page_id: str = ""
    meta_page_access_token: str = ""
    meta_api_base_url: str = "https://graph.facebook.com/v19.0"
    llm_provider: str = "mock"
    openai_api_key: str = ""
    jwt_secret: str = "change-me"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
