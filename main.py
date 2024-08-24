from aiogram import Bot, Dispatcher

from config import TOKEN
import setup

bot = Bot(token=(TOKEN))
dp = Dispatcher()

if __name__ == "__main__":
    dp.run_polling(bot)
