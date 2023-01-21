from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton('Хочу пистолет'),
    KeyboardButton('Хочу автомат'),
    KeyboardButton('Хочу полуавтомат')
)

async def shop_start(cb: types.CallbackQuery):
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="Выберите категорию из меню ниже",
        reply_markup=shop_kb
    )

async def addres(cb: types.CallbackQuery):
    await cb.bot.send_message(chat_id=cb.from_user.id,
                              text="Наш адрес: \n"
                                   "Бишкек, Ленинский район, \n"
                                   "Цокольный этаж, \n"
                                   "Калык Акиева 102")


