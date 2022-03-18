from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ACCESS_TOKEN_EXPIRE_DAYS: int
    USERS_OPEN_REGISTRATION: bool

    FIRST_SUPER_ADMIN_EMAIL: str
    FIRST_SUPER_ADMIN_PASSWORD: str
    FIRST_SUPER_ADMIN_CLIENT_NAME: str

    SQLALCHEMY_DATABASE_URI: str

    class Config:
        case_sensitive = True
        env_file = ".env.sample"


def get_settings():
    return Settings()


settings = get_settings()
