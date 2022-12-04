from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Регистрация'),
            BotCommand('personal_account', 'Личный кабинет'),
            BotCommand('reports', 'Отчеты'),
            BotCommand('faq', 'FAQ')
        ]
    )
