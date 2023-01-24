from aiogram import types
from handler.constants import START_TEXT
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(InlineKeyboardButton('Магазин', callback_data='shop_start'),
             InlineKeyboardButton('Наш адрес', callback_data='addres'))
start_kb.add(InlineKeyboardButton('Анкета', callback_data='form'))


async def start_command(message: types.Message):
    """
    Функция приветствия
    """
    await message.answer(
        text=START_TEXT.format(
          first_name=message.from_user.first_name),
        reply_markup=start_kb)
    await message.delete()