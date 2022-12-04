from aiogram import Dispatcher, types

from bot.handlers.user.keyboards.inline.callback_data.report_callback_data import seller_report
from bot.handlers.user.keyboards.inline.report_inline import report_inline
from database.users.models.user_model import User


async def reports_command(message: types.Message):
    user = User.get_or_none(User.user_id == message.from_user.id)

    if user:
        await message.answer(text='Отчеты', reply_markup=report_inline)
    else:
        await message.answer(text='Вы не зарегистрированы')


async def seller_report_callback(call: types.CallbackQuery):
    await call.message.answer('a')


def register_handler_report(dp: Dispatcher):
    dp.register_message_handler(reports_command, commands='reports')

    dp.register_callback_query_handler(seller_report_callback, seller_report.filter())
