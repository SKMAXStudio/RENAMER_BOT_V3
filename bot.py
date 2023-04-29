import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6291649683:AAG-T-wddjXn2PC_FIVujMEXyKk2pDqTJuc")

API_ID = int(os.environ.get("API_ID", "29034718"))

API_HASH = os.environ.get("API_HASH", "5719d4400fd38bf1eb353d05174562ed")

STRING = os.environ.get("STRING", "@SKMAX_Studio")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
