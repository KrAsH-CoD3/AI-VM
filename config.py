from dotenv import load_dotenv
from os import environ as env_variable

load_dotenv()

class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    OPENAI_KEY = env_variable.get('OPENAIKEY')

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
