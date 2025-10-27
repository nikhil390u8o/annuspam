import logging
from telethon import TelegramClient
from os import getenv
from AltBots.data import ALTRON

# Logging setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Telegram API details
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Bot Tokens (only one active)
BOT_TOKEN = "7831768261:AAEdj_WXI4uZlGetoiecvROGMWT4vosCi6E"
BOT_TOKEN2 = None
BOT_TOKEN3 = None
BOT_TOKEN4 = None
BOT_TOKEN5 = None
BOT_TOKEN6 = None
BOT_TOKEN7 = None
BOT_TOKEN8 = None
BOT_TOKEN9 = None
BOT_TOKEN10 = None

# Owner and Sudo users
SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5518687442").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6079943111"))
SUDO_USERS.append(OWNER_ID)

# Initialize only one active bot client
X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


