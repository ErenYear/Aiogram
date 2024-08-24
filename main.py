import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import TOKEN
import setup

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()

async def on_startup(dp: Dispatcher):
    print("Bot has started successfully.")

async def on_shutdown(dp: Dispatcher):
    print("Bot is shutting down.")

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


asyncio.run(main())
