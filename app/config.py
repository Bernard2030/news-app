class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?q=&apiKey={}'
   
class Prodconfig(Config):
    """
    Production configuration child class.

    Args: The parent configuration class with the General configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuratrion child class.

    Args:
        Config: The parent configuration class with General configuratrion settings 
    """


    DEBUG = True
