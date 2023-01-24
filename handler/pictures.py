from aiogram import types

async def image_sender(message: types.Message):
    """
    Функция показывает картинку
    """
    await message.answer_photo(
        open('images/pp-katana-01-1.jpg', 'rb'))
    await message.delete()
