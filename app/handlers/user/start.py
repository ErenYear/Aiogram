from aiogram.types import Message
from aiogram.filters import Command

from app.routers import start_router as start

@start.message(Command("start"))
async def user_start(message: Message):
    await message.reply("Welcome!")
    
