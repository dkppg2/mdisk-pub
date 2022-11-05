from configs import Config
from ffmpeg.access_db import db
from pyrogram import Client
from pyrogram.types import Message


async def AddUserToDatabase(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_message(
                int(Config.LOG_CHANNEL),
                f"**New User:** [{cmd.from_user.first_name}](tg://user?id={str(cmd.from_user.id)})\n**Username:** `{cmd.from_user.username}`\n**UserID:** `{cmd.from_user.id}` started @{(await bot.get_me()).username} !!"
            )
