import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "22672907"))
API_HASH = environ.get("API_HASH", "0ff15ae2153bd8e03b48cb293010bc6a")
BOT_TOKEN = environ.get("BOT_TOKEN", "7087741098:AAFhQ6yKXdScmNcKPlutvHL1sHhUKdb5dws")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002022119783"))
ADMINS = int(environ.get("ADMINS", "6287591671"))
DB_URI = environ.get("DB_URI", "mongodb+srv://rani828719:sVyRWZOrUzIWNfHp@cluster0.zodktob.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptHErobot")
OPENAI_API = environ.get("OPENAI_API", "sk-proj-DhpiKsXCHE09EWYeMkA4T3BlbkFJf46borWbVw5v7dYv3Dkz")
AI = is_enabled((environ.get("AI","True")), False)
