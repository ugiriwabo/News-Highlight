class Config:
#    https://newsapi.org/v2/sources?apiKey=62d3d0fc90f44f239b70a7216f8525a3
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
#    https://newsapi.org/v2/sources?category={}&apiKey={}
# https://newsapi.org/v2/sources?language=en&category={}&apiKey={}
    pass

class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True