# (©)Codexbotz

import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5956021918:AAHcFpgfZUjPQ3ElB8Ko1F5Tej2-QMEhX5Q")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11698078"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "cdab9ff055e4eb433fc4bd771d143298")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001810517856"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5589797950"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "gkushskap")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://xupwbxxa:4SCfAzGvy4xpj9P3VzuBfPn4AsgasV-T@rosie.db.elephantsql.com/xupwbxxa")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "none")
GROUP = os.environ.get("GROUP", "none")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001857187402"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001673770607"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>JOIN VVIP MURAH DAN TERPERCAYA DI @VIPEXOTIS.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nJOIN VVIP MURAH DAN TERPERCAYA DI @VIPEXOTIS\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(5589797950)
ADMINS.append(1245451624)
ADMINS.append(1780709155)
ADMINS.append(1715348447)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
