import os


class Config(object):
    API_ID = os.environ.get("API_ID", "15050363")
    API_HASH = os.environ.get("API_HASH", "209169a882ff43c4f1621b7cc97c255b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5544101630:AAG1IB4ASSo2iRNy7NE09qOzcos6PkqCx00")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Mdisk-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001679764868")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://john-abu11:ooz4PXFbWBV3OLIs@cluster0.mhlqpbe.mongodb.net/?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 660755963))

    START_TEXT = """
Hi Unkil, I am Mdisk Bot!

"""
    CAPTION = "Mdisk Bot by @{}\n\nMade by @"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
