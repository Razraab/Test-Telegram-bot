import random
from aiogram import Dispatcher
from aiogram.types import Message

START_MESSAGES = [
    """
Hello this is bot for testing on python
developer, i can create meme from photo!
<b>Just send for me and add font size in
description😉</b>
""",
    """
Hi! I am bot made for testing) My task
is create meme from photo!
<b>Just send for me and add font size in
description😉</b>""",
    """
Hi! This is a bot for creating memes from 
photos sent by you🥑 - Perfect avocado.
<b>Just send for me and add font size in
description😉</b>
"""]

JUST_MESSAGES = [
    'Stop writing nonsense!',
    'send a picture, not a text.',
    'You\'re so fucking stupid!'
]
count = 0


async def start_handler(message: Message):
    await message.answer(random.choice(START_MESSAGES), parse_mode='HTML')


async def talk_handler(message: Message):
    global count
    count += 1
    if 5 < count:
        await message.answer(random.choice(JUST_MESSAGES), parse_mode='HTML')


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(commands=['start'], callback=start_handler)
    dp.register_message_handler(callback=talk_handler)