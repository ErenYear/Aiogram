from aiogram.types import Message

from main import dp


@dp.message(commands="start")
async def user_start(message: Message):
    await message.reply("Welcome!")
