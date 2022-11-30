from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.handlers.user.states.registration_user_state import RegistrationUserState
from database.code.code_data_store import validation_code
from database.users.user_data_store import create as create_user


async def start_bot(message: types.Message):
    user = message.from_user
    await message.answer('Привет, {}!'.format(user.username or user.first_name or user.last_name))
    await message.answer('Введите код доступа')
    await RegistrationUserState.EnterCode.set()


async def enter_code_state(message: types.Message, state: FSMContext):
    code = message.text

    code_validation = validation_code(valid_code=code)

    if code_validation:
        await message.answer(text='Код успешно подошел. Введите токен')
        await state.update_data(code=code)
        await RegistrationUserState.next()
    else:
        await message.answer(text='Код не действителен')


async def enter_token_state(message: types.Message, state: FSMContext):
    data = await state.get_data()
    code = data.get('code')
    token = message.text

    if len(token) >= 64:
        user_login = message.from_user.username or message.from_user.last_name or message.from_user.first_name
        await create_user(user_id=message.from_user.id, login=user_login, code=code, token=token)
        await message.answer(text='Успешно. Добро пожаловать')
    else:
        await message.answer(text='Токен неверный')


def register_handler_registration_user(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'], state='*')
    dp.register_message_handler(enter_code_state, state=RegistrationUserState.EnterCode)
    dp.register_message_handler(enter_token_state, state=RegistrationUserState.EnterToken)
