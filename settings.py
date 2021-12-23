from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_CONFIG = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///./blog.db"
    }


settings = Settings()
