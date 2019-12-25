import os
import time
import logging

import telebot
from telebot import apihelper

# Logger
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# Set proxy
apihelper.proxy = {'http': TG_PROXY}

# Init bot
bot = telebot.TeleBot(TG_BOT_TOKEN)
