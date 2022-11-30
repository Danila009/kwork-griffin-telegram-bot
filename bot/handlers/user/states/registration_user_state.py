from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationUserState(StatesGroup):
    EnterCode = State()
    EnterToken = State()
