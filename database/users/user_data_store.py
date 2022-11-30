from database.users.models.user_model import User

from datetime import datetime


async def create(user_id: str, login: str, code: str, token: str):
    user = User.get_or_none(User.user_id == user_id)

    if not user:
        date = datetime.now()
        User.create(user_id=user_id, login=login, code=code, token=token, create_date=date)
