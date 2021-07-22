class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    MESSAGE = 'Product'


class DevelopmentConfig(Config):
    DEBUG = True
    MESSAGE = 'Development'


class TestingConfig(Config):
    TESTING = True
    MESSAGE = 'Testing'


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)