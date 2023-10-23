from aiogram import Router, F, types
from aiogram.types import FSInputFile
from keyboards.back import get_back_kb

router = Router()


@router.callback_query(F.data == 'top')
async def top(callback: types.CallbackQuery):
    keyboard = get_back_kb()
    image = FSInputFile('img/top.png')
    caption = 'Список лучших:'
    # res = await get_best_and_player() 10 order_by rating and player
    await callback.message.edit_caption(caption=caption, reply_markup=keyboard, image=image)

