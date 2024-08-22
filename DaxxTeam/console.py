import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", "21767752"))
API_HASH = getenv("API_HASH", "8817c95b20fca899462336cdf36dd958")
BOT_TOKEN = getenv("BOT_TOKEN", "7178919717:AAE-B5nEhE8GBLfBHFD0eL1AvDJiVnV3duM")
STRING_SESSION = getenv("STRING_SESSION", "BQFMJkgADijzuJOv-qLbJS9OaD3BmMvNUqG8zYADGXlvzwRFCl7RmrCBYeckQj3l9W5jCeR71EMQCQku7KjWLl0IEXI_kcI8H71tri81YzdYd-v-uaE5TqEqM-t-y4MKT9THVTkXlupqNmEkewxP_i8jJraykH6ddacfp1oKRwm0aDy-e1Tqbip3VDRsOjkcTjSiO-AbrSV9j_lwgY_-XMIKPO9dUqpIk-BtG2sMLHXNYV2EHZmcSdQxVGpfAFSax8crseCjI0JEDx4c0XkPhDB_wWSuvWDUe_nAi_bdx4GoY0d-Ws5nznclgffyUPzwt9MA9Rm2UUm6hK_4iKWAB37_aF9cxQAAAAE5zUGcAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Sarkar123:GAUTAMMISHRA@sarkar.1uiwqkd.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002242282030"))


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", "BQFMJkgADijzuJOv-qLbJS9OaD3BmMvNUqG8zYADGXlvzwRFCl7RmrCBYeckQj3l9W5jCeR71EMQCQku7KjWLl0IEXI_kcI8H71tri81YzdYd-v-uaE5TqEqM-t-y4MKT9THVTkXlupqNmEkewxP_i8jJraykH6ddacfp1oKRwm0aDy-e1Tqbip3VDRsOjkcTjSiO-AbrSV9j_lwgY_-XMIKPO9dUqpIk-BtG2sMLHXNYV2EHZmcSdQxVGpfAFSax8crseCjI0JEDx4c0XkPhDB_wWSuvWDUe_nAi_bdx4GoY0d-Ws5nznclgffyUPzwt9MA9Rm2UUm6hK_4iKWAB37_aF9cxQAAAAE5zUGcAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 Hey, I am an advanced & superfast high quality userbot assistant with an upgraded version security system.\n\n🌿 I can't let you message my owner's dm without my owner's permission.\n\n🌺 My owner is offline now, please wait until my owner allows you.\n\n🍂 Please don't spam here, because spamming will force me to block you from my owner id.**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://graph.org/file/1217cb1e402b99fa47fdf.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Daxx")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = [5247304559]


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

