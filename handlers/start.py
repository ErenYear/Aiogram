from main import dp


@dp.message_handler(commands="start")
async def user_start(message: Message):
    await message.reply("Welcome!")
