from aiogram import types
from handler.constants import CURSES_TEXT

async def example(message: types.Message):
    print(f"{message.chat.type=}")
    print(f"{message.reply_to_message=}")
    print(f"{message.from_user.id=}")
    if message.chat.type != 'private':
        admins = await message.chat.get_administrators()