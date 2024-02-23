from aiogram import Bot, Dispatcher

from config import Config
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router
import asyncio


async def main():
    # Bot and Dispatcher setup
    bot = Bot(token=Config.TELEGRAM_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
