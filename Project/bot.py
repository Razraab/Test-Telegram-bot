import os
from aiogram import Bot, Dispatcher

bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot=bot)