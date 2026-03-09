from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DreamMakeovers API"
    environment: str = "development"
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24

    database_url: str = "postgresql+psycopg2://postgres:postgres@db:5432/dreammakeovers"
    frontend_url: str = "http://localhost:3000"

    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    aws_s3_bucket: str = ""
    aws_region: str = "ap-south-1"

    razorpay_key_id: str = ""
    razorpay_key_secret: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
