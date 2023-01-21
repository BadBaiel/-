from aiogram import types
from handler.constants import HELP_TEXT



async def help_command(message: types.Message):
    """
    Функция показывает все команды
    """
    await message.answer(
        text=HELP_TEXT.format(
            first_name=message.from_user
        ))
    await message.delete()