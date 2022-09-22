from pydantic import BaseSettings


class DBConfig:
    HOST: str = 'localhost'
    USER: str = 'uttam'
    PASSWORD: str = ''
    NAME: str = 'fastapi'
    DATABASE: str = 'postgresql'


class Config(BaseSettings):
    HOST: str = 'localhost'
    PORT: int = 8080
    DATABASE_URL: str = f'{DBConfig.DATABASE}://{DBConfig.USER}:{DBConfig.PASSWORD}@{DBConfig.HOST}/{DBConfig.NAME}'
    RABBITMQ_SERVER: str = 'amqp://guest:guest@localhost/'
    ALLOWED_TOPICS: list = [
        'register'
    ]


config = Config()
