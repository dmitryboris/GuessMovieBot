import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiologger.loggers.json import JsonLogger
from dotenv import load_dotenv, find_dotenv
from data import db_session
from handlers import start, top, about

load_dotenv(find_dotenv())


async def main():
    logger = JsonLogger.with_default_handlers(
        level=logging.INFO,
    )

    bot = Bot(token=os.getenv('TOKEN'), disable_web_page_preview=True)

    # await db_session.global_init('db/')

    description = ''
    await bot.set_my_description(description=description)

    dp = Dispatcher()
    dp.include_routers(start.router, top.router, about.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
