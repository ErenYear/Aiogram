from aiogram.types import Message
from aiogram.filters import Command

from main import dp

@dp.message(Command(["lund"]))
async def user_start(message: Message):
    await message.reply("Welcome!")
    
