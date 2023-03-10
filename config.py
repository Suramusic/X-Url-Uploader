import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5713245787:AAF-x7x7vbxcWO98HFbrkPI8FDIH24iw4Ww")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", "24531402"))
    API_HASH = os.environ.get("API_HASH", "0f75926e95a476ccff47dacb52079053")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1471469091").split())
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1471469091").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001740477053")
    # Log Channel ID
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001740477053"))
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # database url
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Tamilbots:tamilbots@cluster0.aa2e1nd.mongodb.net/?retryWrites=true&w=majority")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Tamilbots")
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/83d3d122a961203de05ab.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = "Alinallmovies"
