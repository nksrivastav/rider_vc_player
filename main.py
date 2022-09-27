import asyncio
from pytgcalls import idle
from Zaid.Database import db

import os
import sys
import random
import asyncio
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2
from pyrogram import Client
from pytgcalls import PyTgCalls
from Rider.main import *



loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
import asyncio

from time import time

from datetime import datetime

from modules.helpers.filters import command

from modules.helpers.command import commandpro

from pyrogram import Client, filters

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

START_TIME = datetime.utcnow()

START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()

TIME_DURATION_UNITS = (

    ('week', 60 * 60 * 24 * 7),

    ('day', 60 * 60 * 24),

    ('hour', 60 * 60),

    ('min', 60),

    ('sec', 1)

)

async def _human_time_duration(seconds):

    if seconds == 0:

        return 'inf'

    parts = []

    for unit, div in TIME_DURATION_UNITS:

        amount, seconds = divmod(int(seconds), div)

        if amount > 0:

            parts.append('{} {}{}'

                         .format(amount, unit, "" if amount == 1 else "s"))

    return ', '.join(parts)

    

   

   

@Client.on_message(command("start") & filters.private & ~filters.edited)

async def start_(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://telegra.ph/file/b93274f340d94dac0c1ef.jpg",

        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━

💫🙈🙈 𝙔𝙚 𝙩𝙜 𝙠𝙖 𝙗𝙚𝙨𝙩 𝙢𝙪𝙨𝙞𝙘 𝙗𝙤𝙩 𝗵𝙖𝙞 𝙟𝙤 𝙡𝙖𝙜 𝙛𝙧𝙚𝙚 𝙢𝙪𝙨𝙞𝙘 𝙗𝙖𝙟𝙖𝙮𝙚𝙜𝙖

𝙖𝙥𝙠𝙚 𝙫𝙘 𝙢𝙚𝙞𝙣🙄.𝙊𝙬𝙣𝙚𝙧:- 𝙬𝙖𝙧𝙧𝙞𝙤𝙧 𝐑𝐢𝐃𝐄𝐑  ...

┏━━━━━━━━━━━━━━━━━┓

┣★ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁: [𝐖𝐀𝐑𝐑𝐈𝐎𝐑](https://t.me/+1q7zmqi5sBtiNWY1)

┣★ 𝐎𝐖𝐍𝐄𝐑: [@Masoom_banda]

┣★ 𝗚𝗿𝗼𝘂𝗽 : [𝐖𝐀𝐑𝐑𝐈𝐎𝐑](https://t.me/+1q7zmqi5sBtiNWY1)

┗━━━━━━━━━━━━━━━━━┛

𝗔𝗴𝗮𝗿 𝗮𝗽𝗸𝗼 𝗸𝗼𝗶 𝗱𝗶𝗸𝗸𝗮𝘁 𝗮𝗿𝗶 𝘁𝗼𝗵 𝗶𝗱𝗵𝗮𝗿 𝗷𝗮𝗸𝗲 𝗼𝘄𝗻𝗲𝗿 𝘀𝗲

𝗰𝗼𝗻𝘁𝗮𝗰𝘁 𝗸𝗮𝗿𝗲😍 [𝐑𝐢𝐃𝐄𝐑](@masoom_banda)(https://t.me/+1q7zmqi5sBtiNWY1)...

━━━━━━━━━━━━━━━━━━━━━━━━**""",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "🥳𝙊𝙬𝙣𝙚𝙧 𝙞𝙙𝙝𝙖𝙧 𝙢𝙞𝙡𝙚𝙣𝙜𝙚🤩", url=f"https://t.me/+1q7zmqi5sBtiNWY1")

                ]

                

           ]

        ),

    )

    

    

@Client.on_message(commandpro(["/start"]) & filters.group & ~filters.edited)

async def start(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://telegra.ph/file/b93274f340d94dac0c1ef.jpg",

        caption=f"""""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "𝙅𝙤𝙞𝙣 𝙠𝙖𝙧𝙡𝙤 𝙮𝙧𝙡", url=f"https://t.me/Blue_warrior_riders")

                ]

            ]

        ),

    )

@Client.on_message(commandpro(["repo"]) & filters.group & ~filters.edited)

async def help(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://telegra.ph/file/IMG_20220828_152532_622.jpg",

        caption=f"""""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "🙄𝙍𝙚𝙥𝙤 𝙠𝙮𝙪 𝙘𝙝𝙖𝙝𝙞𝙮𝙚🤔", url=f"https://telegra.ph/file/146be6929217e4efbe12e.jpg")

                ]

            ]

        ),

    )

