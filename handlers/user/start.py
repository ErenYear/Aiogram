from aiogram.types import Message
from aiogram.filters import Command
from handlers import app

@app.message(Command("lund"))
async def user_start(message: Message):
    await message.reply("Welcome!")
    
