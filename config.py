import os

class Config:

    MOVIE_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey=e984567f65124d82bdb23cfc40ce31b8'
    MOVIE_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}