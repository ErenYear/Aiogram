from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

from main import dp

lunduser = Router()

@lunduser.message(Command(["lund"]))
async def user_start(message: Message):
    await message.reply("Welcome!")
    
