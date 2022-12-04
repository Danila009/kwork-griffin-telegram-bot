from aiogram.dispatcher.filters.state import StatesGroup, State


class UpdateTokenState(StatesGroup):
    EnterNewToken = State()
