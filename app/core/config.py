from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        case_sensitive = True
        env_file = ".env.sample"


def get_settings():
    return Settings()


settings = get_settings()
