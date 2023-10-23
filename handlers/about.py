from aiogram import Router, F, types
from aiogram.types import FSInputFile
from keyboards.back import get_back_kb

router = Router()


@router.callback_query(F.data == 'about')
async def about(callback: types.CallbackQuery):
    keyboard = get_back_kb()
    image = FSInputFile('img/start.png')
    caption = 'что-то про игру'
    await callback.message.edit_caption(caption=caption, reply_markup=keyboard)
    # await callback.message.answer_photo(image, caption=caption, reply_markup=keyboard)
