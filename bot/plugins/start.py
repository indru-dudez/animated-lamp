from pyrogram import filters as  Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
    
    await m.reply_text(
        text=f"Hi there {m.from_user.first_name}.\n\nI'm Screenshot Generator Bot. I can provide screenshots from your video files with out downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Source 😒', url='https://t.me/Torrent_To_Files'),
                    InlineKeyboardButton('Project Channel', url='https://t.me/BlueSkyMovie')
                ],
                [
                    InlineKeyboardButton('My Father', url='https://t.me/SI_NN_ER_LS')
                ]
            ]
        )
    )
