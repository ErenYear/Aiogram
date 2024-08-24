from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

help = Router()

@app.message(Command("help"))
async def help_command(message: Message):
    help_text = (
        "Here are some commands you can use:\n"
        "/start - Start interacting with the bot\n"
        "/help - Get a list of available commands\n"
        "/info - Get information about this bot\n"
        "/lund - A fun command to welcome you"
    )
    await message.reply(help_text)
