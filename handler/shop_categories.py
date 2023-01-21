from aiogram import types, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(
    InlineKeyboardButton('Купить', callback_data='buy_item'
))

async def show_gun(message: types.Message, ):
    """Показывет список пушек
    """
    await message.answer(text="Пистолет", reply_markup=buy_item_kb)
    await message.answer_photo(
        open('images/original_90642d661935494e9f6d7ffb5dc637fe.jpg', 'rb'))
async def show_weapon(message: types.Message):
    await message.answer(text="Автомат ", reply_markup=buy_item_kb)
    await message.answer_photo(
        open('images/fonn-d67407726270f7fe8b56a0e3f9fe68f1.jpg', 'rb'))
async def show_semiautomatic_weapon(message: types.Message):
    await message.answer(text="Полуавтомат ", reply_markup=buy_item_kb)
    await message.answer_photo(
        open('images/4345720.jpg', 'rb'))


