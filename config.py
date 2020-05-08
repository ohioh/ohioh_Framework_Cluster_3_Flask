import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MONGO_URI = '{}/{}'.format(os.getenv('DB_CONNECTION_URL'),os.getenv("DB_NAME"))