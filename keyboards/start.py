from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


def get_start_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    buttons_text = {'Играть': 'play', 'Топ игроков': 'top', 'Об игре': 'about'}
    for text in buttons_text:
        builder.row(InlineKeyboardButton(text=text, callback_data=buttons_text[text]))
    return builder.as_markup()


def get_start_game_kb(buttons_text: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(0, len(buttons_text), 2):
        builder.row(InlineKeyboardButton(text=buttons_text[i], callback_data=buttons_text[i]),
                    InlineKeyboardButton(text=buttons_text[i + 1], callback_data=buttons_text[i]))
    return builder.as_markup()
