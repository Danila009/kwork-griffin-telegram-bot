from aiogram import types

from bot.handlers.user.keyboards.inline.callback_data.report_callback_data import warehouse_condition, seller_report

report_inline = types.InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text='Сводный отчет продавца',
                callback_data=seller_report.new()
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Состояние склада',
                callback_data=warehouse_condition.new()
            )
        ]
    ]
)
