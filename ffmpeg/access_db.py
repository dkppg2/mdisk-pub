from configs import Config
from ffmpeg.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
