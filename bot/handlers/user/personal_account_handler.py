from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from bot.handlers.user.states.update_code_state import UpdateCodeState
from database.users import user_data_store

from bot.handlers.user.keyboards.inline.callback_data.personal_account_callback_data import personal_account_settings, \
    inline_back, settings_update_token, update_code, personal_account_code
from bot.handlers.user.keyboards.inline.personal_account_inline import personal_account_inline, \
    settings_update_token_inline, update_code_inline
from bot.handlers.user.states.update_token_state import UpdateTokenState
from database.users.models.user_model import User


async def personal_account_command(message: types.Message):
    user = User.get_or_none(User.user_id == message.from_user.id)

    if user:
        await message.answer(text='Личный кабинет', reply_markup=personal_account_inline)
    else:
        await message.answer(text='Вы не зарегистрированы')


async def personal_account_settings_callback(call: types.CallbackQuery):
    await call.message.edit_text('Настройки личного кабинета')
    await call.message.edit_reply_markup(settings_update_token_inline)


async def settings_update_token_callback(call: types.CallbackQuery):
    await call.message.answer(text='Введите новый токен')
    await UpdateTokenState.EnterNewToken.set()


async def enter_new_token_state(message: types.Message, state: FSMContext):
    token = message.text

    if len(token) >= 64:
        await user_data_store.update_token(user_id=message.from_user.id, new_token=token)
        await message.answer(text='Токен обновлен')

        await state.finish()
    else:
        await message.answer(text='Токен неверный')


async def personal_account_code_callback(call: types.CallbackQuery):
    await call.message.edit_text('Код доступа')
    await call.message.edit_reply_markup(update_code_inline)


async def update_code_callback(call: types.CallbackQuery):
    await call.message.answer(text='Введите новый код')
    await UpdateCodeState.EnterNewCode.set()


async def enter_new_code_state(message: types.Message, state: FSMContext):
    code = message.text

    update_code_message = await user_data_store.update_code(user_id=message.from_user.id, new_code=code)
    await message.answer(text=update_code_message)

    await state.finish()


async def inline_back_callback(call: types.CallbackQuery, callback_data: dict):
    inline = callback_data.get('inline')

    if inline == 'personal_account':
        await call.message.edit_text('Личный кабинет')
        await call.message.edit_reply_markup(personal_account_inline)


def register_handler_personal_account(dp: Dispatcher):
    dp.register_message_handler(personal_account_command, commands="personal_account")

    dp.register_callback_query_handler(personal_account_settings_callback,
                                       personal_account_settings.filter())
    dp.register_callback_query_handler(settings_update_token_callback, settings_update_token.filter())

    dp.register_callback_query_handler(personal_account_code_callback,
                                       personal_account_code.filter())
    dp.register_callback_query_handler(update_code_callback, update_code.filter())

    dp.register_callback_query_handler(inline_back_callback, inline_back.filter())

    dp.register_message_handler(enter_new_token_state, state=UpdateTokenState.EnterNewToken)
    dp.register_message_handler(enter_new_code_state, state=UpdateCodeState.EnterNewCode)
