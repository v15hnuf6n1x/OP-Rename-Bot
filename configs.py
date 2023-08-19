# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "21165589"))
    API_HASH = os.environ.get("API_HASH", "8cc762f4873e84a7cf0cbfd66a07244b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6458881761:AAGpnLADPVGuRiUqiJOR6Bjb393Cpr2YmJs")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 2048030675))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Erogire:erogirelad@cluster1.boyfnr5.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001869648454"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
