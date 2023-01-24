from aiogram import types, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(
    InlineKeyboardButton('Купить', callback_data='buy_item'
))

async def show_gun(message: types.Message):
    """Показывет список пушек
    """
    await message.answer_photo(open('./images/original_90642d661935494e9f6d7ffb5dc637fe.jpg', 'rb'), caption="Пистолет\n"
                                                                                                             "Цена-25 000\n"
                                                                                                             "Полный комплект",
                               reply_markup=buy_item_kb)
async def show_weapon(message: types.Message):
    await message.answer_photo(open('./images/fonn-d67407726270f7fe8b56a0e3f9fe68f1.jpg', 'rb'),caption="автомат\n"
                                                                                                        "Цена-55 000\n"
                                                                                                        "Полный комплект",
                               reply_markup=buy_item_kb)
async def show_semiautomatic_weapon(message: types.Message):
    await message.answer_photo(open('images/4345720.jpg', 'rb'), caption="автомат\n"
                                                                         "Цена-55 000\n"
                                                                         "Полный комплект",
                                    reply_markup=buy_item_kb)


