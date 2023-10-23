from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


def get_start_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    buttons_text = {'Играть': 'play', 'Топ игроков': 'top', 'Об игре': 'about'}
    for text in buttons_text:
        builder.row(InlineKeyboardButton(text=text, callback_data=buttons_text[text]))
    return builder.as_markup()

