# Author: Jigarvarma2005

from os import environ, path
from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")

class Config(object):
    BOT_TOKEN = environ.get('BOT_TOKEN', "7811050565:AAHXn1xFfRBsYYwWcUWcmxDU57-aquvvXQA")
    API_ID = int(environ.get('API_ID', 28735016))
    API_HASH = environ.get('API_HASH', "395761ed41e18de91ee4e18ff99afc81")
    MONGO_DB_URI = environ.get('MONGO_DB_URI', "mongodb+srv://kalawativerma80:<db_password>@cluster0.vxnio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
