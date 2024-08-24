from aiogram.types import Message
from aiogram.filters import Command
from main import app

@app.message(Command("lund"))
async def user_start(message: Message):
    await message.reply("Welcome!")
    
