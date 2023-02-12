import asyncio

from aiogram import Bot, Dispatcher, types
import logging

from aiogram.fsm.storage.memory import MemoryStorage

from config import CONFIG
from routes import default, kittens

bot = Bot(token=CONFIG.TELEGRAM_API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)

dp.include_router(default.router)
dp.include_router(kittens.router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
