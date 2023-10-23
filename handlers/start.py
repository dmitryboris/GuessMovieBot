from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from keyboards.start import get_start_kb

router = Router()


@router.message(Command('start'))
@router.callback_query(F.data == 'menu')
async def start(message: types.Message or types.CallbackQuery):
    keyboard = get_start_kb()
    image = FSInputFile('img/start.png')
    greetings = "Меню. Это бот 'Угадай фильм по картинке'"
    if type(message) == types.Message:
        name = message.from_user.first_name
        print(message.from_user)
        greetings = f"Меню. Привет, {name}! Это бот 'Угадай фильм по картинке'. ОГО!"
        """user = None
        if not user:
            await add_user(message.from_user.id, message.from_user.first_name)"""
        await message.answer_photo(image, caption=greetings, reply_markup=keyboard)
    elif type(message) == types.CallbackQuery:
        await message.message.edit_caption(caption=greetings, reply_markup=keyboard, image=image)

