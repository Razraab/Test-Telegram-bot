import os
import json
import random

from datetime import datetime
import aiofiles

from bot import bot
from .image_editor_package.image_editor import ImageEditor

from aiogram import Dispatcher
from aiogram.types import Message


async def photo_handler(message: Message):
    now = datetime.now()
    path = f'{os.getcwd()}\\edited_photos\\{message.from_user.id}'
    filename = f'\\{datetime.now().strftime("%Y-%m-%d_%H-%M")}_{message.from_user.id}' + '.jpg'
    if not os.path.exists(path):
        os.mkdir(path)

    await message.photo[-1].download(destination_file=path+filename)
    # Edit photo
    try:
        async with aiofiles.open(f'{os.getcwd()}\\data\\joke.json', 'r', encoding='utf-8') as f:
            ImageEditor.draw(path=path+filename,
                            text=random.choice(json.loads(await f.read())),
                            fontsize=int(message.caption))
    except TypeError:
        await message.answer('In caption write number\n'
                             'which will font size')
        return
    # Send edited photo to user
    async with aiofiles.open(path+filename, 'rb') as f:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=await f.read())


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(content_types=['photo'], callback=photo_handler)