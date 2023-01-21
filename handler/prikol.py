from aiogram import types, Dispatcher
from config import bot

from handler.all_messages import echo
from handler.constants import CURSES_TEXT


async def check_curses(message: types.Message):
    bad_words = ['дурак', 'тупой', 'плохой', 'тупица']
    username = f"@{message.from_user.username}" \
        if message.from_user.username is not None else message.from_user.first_name
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.delete()
            await message.answer(f'Плохие слова не делают тебя элегантным,'
                                 f'лучше извинись {username}.')
            await message.answer(text=CURSES_TEXT.format(
                first_name = message.from_user.first_name))

def register_hendlers(dp: Dispatcher):
    dp.register_message_handler(echo)
