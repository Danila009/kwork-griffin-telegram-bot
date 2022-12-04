from database.code.code_data_store import validation_code
from database.users.models.user_model import User

from datetime import datetime


async def create(user_id: str, login: str, code: str, token: str) -> bool:
    user = User.get_or_none(User.user_id == user_id)

    if not user:
        date = datetime.now()
        User.create(user_id=user_id, login=login, code=code, token=token, create_date=date)
        return True
    else:
        return False


async def update_token(user_id: int, new_token: str):
    qry = User.update({User.token: new_token}).where(User.user_id == user_id)
    qry.execute()


async def update_code(user_id: int, new_code: str) -> str:
    user = User.get_or_none(User.user_id == user_id)

    if user:
        valid_code = validation_code(new_code)

        if valid_code:
            qry = User.update({User.code: new_code}).where(User.user_id == user_id)
            qry.execute()
            return 'Успешно'
        else:
            return 'Код не действителен'
    else:
        return 'Пользователь не найден'

