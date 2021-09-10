class Config:
    """
    General configuration parent class
    """
    pass

class Prodconfig(Config):
    """
    Production configuration child class.

    Args: The patrent configuration class with the General configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuratrion child class.

    Args:
        Config: The parent configuration class with General configuratrion settings 
    """


    DEBUG = True
