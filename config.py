from dotenv import load_dotenv
import os
import dotenv

dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)


class Config:
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = 'development'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///dog.db'

class ProductionConfig(Config): pass
