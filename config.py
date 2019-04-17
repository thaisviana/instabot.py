import os
import dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '53cr3t_k3y')
    CORS_HEADERS = 'Content-Type'


class ProductionConfig(Config):
    DEBUG = False
