import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.data.config import BOT_TOKEN
from bot.handlers.errors.errors_handler import register_errors_handler
from bot.handlers.user.registration_user_handler import register_handler_registration_user
from database.database import create_database

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())


def register_all_handlers():
    register_handler_registration_user(dp)
    register_errors_handler(dp)


async def set_all_default_commands():
    pass


async def on_startup():
    create_database()


async def on_shutdown(_):
    await bot.delete_webhook()


async def main():
    try:
        logging.basicConfig(level=logging.INFO)

        await set_all_default_commands()
        register_all_handlers()

        await on_startup()
        await dp.start_polling()

        await bot.get_webhook_info()
    finally:
        await bot.delete_webhook()
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
