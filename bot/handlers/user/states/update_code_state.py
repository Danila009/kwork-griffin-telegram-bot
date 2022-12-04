from aiogram.dispatcher.filters.state import StatesGroup, State


class UpdateCodeState(StatesGroup):
    EnterNewCode = State()
