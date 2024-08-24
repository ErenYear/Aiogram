import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import TOKEN
from handlers.user.start import start
from handlers.user.help import help

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()

async def on_startup():
    print("Bot has started successfully.")

async def on_shutdown():
    print("Bot is shutting down.")

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    setup_handlers(dp)
    await dp.start_polling(bot)


asyncio.run(main())
