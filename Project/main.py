import logging
from aiogram import executor
from handlers import register_user_handlers, register_start_handlers
from bot import dp


def main():
    logging.basicConfig(level=logging.INFO)
    register_user_handlers(dp)
    register_start_handlers(dp)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()