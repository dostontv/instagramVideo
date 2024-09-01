from os import getenv

from dotenv import load_dotenv

load_dotenv('.env')


class BotConfig:
    BOT_TOKEN = getenv('BOT_TOKEN')


class APIConfig:
    API_KEY = getenv('API_KEY')
    API_HOST = getenv('API_HOST')
    API_ENDPOINT = getenv('API_ENDPOINT')
