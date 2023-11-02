from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from keyboards.start import get_start_game_kb

router = Router()


@router.callback_query(F.data == 'play')
async def start_game(callback: types.CallbackQuery):
    keyboard = get_start_game_kb(['Джанго', 'Звездные войны', 'Пираты', 'Лунтик'])
    # await add_game()
    image = FSInputFile('img/1.png')
    caption = "Из какого фильма этот кадр?"

    await callback.message.answer_photo(photo=image, caption=caption, reply_markup=keyboard)
