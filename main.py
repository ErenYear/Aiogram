from aiogram import Bot, Dispatcher
from config import TOKEN

bot = Bot(token=(TOKEN))
dp = Dispatcher()

if __name__ == "__main__":
    dp.run_polling(bot)
