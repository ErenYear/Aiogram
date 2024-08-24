from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

start = Router()

@start.message(Command("start"))
async def user_start(message: Message):
    await message.reply("Welcome!")
    
