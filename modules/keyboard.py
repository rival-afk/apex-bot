from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

reply = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить бота ➕')],
        [KeyboardButton(text='Помощь ℹ️'), KeyboardButton(text='О боте ❔')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Нажми одну из кнопок ниже'
)

inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить в группу➕', url='http://t.me/apexxs_bot?startgroup=apex&admin=change_info+restrict_members+delete_messages+pin_messages+invite_users')]
])