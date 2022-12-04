import datetime

from database.models.base_model import db


def get_count(user_id: int) -> dir:
    today_date = datetime.datetime.today().date()
    yesterday_date = today_date - datetime.timedelta(1)
    week_date = today_date - datetime.timedelta(7)

    today_count = db.execute_sql('SELECT COUNT(*) FROM `{}.telegram_zakaz` WHERE date >= "{}"'
                                 .format(user_id, today_date)).fetchone()[0]

    yesterday_count = db.execute_sql('SELECT COUNT(*) FROM `{}.telegram_zakaz` WHERE "{}" <= date AND date < "{}"'
                                     .format(user_id, yesterday_date, today_date)).fetchone()[0]

    week_date_count = db.execute_sql(
        'SELECT COUNT(*) FROM `{}.telegram_zakaz` WHERE "{}" <= date'.format(user_id, week_date)).fetchone()[0]

    return {'today_count': today_count, 'yesterday_count': yesterday_count, 'week_date_count': week_date_count}
