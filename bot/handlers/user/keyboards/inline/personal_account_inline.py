from aiogram import types

from bot.handlers.user.keyboards.inline.callback_data.personal_account_callback_data import *

personal_account_inline = types.InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text='Бот',
                callback_data=personal_account_bot.new()
            ),
            types.InlineKeyboardButton(
                text='Уведомления',
                callback_data=personal_account_notifications.new()
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Настройки',
                callback_data=personal_account_settings.new()
            ),
            types.InlineKeyboardButton(
                text='Код доступа',
                callback_data=personal_account_code.new()
            )
        ]
    ]
)

settings_update_token_inline = types.InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text='Поменять токен',
                callback_data=settings_update_token.new()
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Назад',
                callback_data=inline_back.new(inline='personal_account')
            )
        ]
    ]
)

update_code_inline = types.InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text='Заменить код доступа',
                callback_data=update_code.new()
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Назад',
                callback_data=inline_back.new(inline='personal_account')
            )
        ]
    ]
)
