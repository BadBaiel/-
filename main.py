import random

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()


bot = Bot(getenv('TG_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def echo(message: types.Message):
    await message.answer(text=f'Привет! {message.from_user.first_name}, я бот! Решил тебя встретить.')
    await message.delete()

@dp.message_handler(commands="help")
async def echo(message: types.Message):
    await message.answer(text=f'Список команд /start-это начало беседы с ботом, /help-это список команд с коротким описанием, /myinfo-это информация о вас, /picture-это показ случайного фото.')
    await message.delete()

@dp.message_handler(commands="myinfo")
async def echo(message: types.Message):
    await message.answer(text=f'Ваш id-{message.from_user.id}, ваш nickname-{message.from_user.first_name}, ваш username-{message.from_user.username}')
    await message.delete()

# @dp.message_handler(commands=["picture"])
# async def image_sender(message: types.Message):
#     await message.answer_photo(
#         open('./images/cat.webp', 'rb'),
#     )
#     await message.delete()
@dp.message_handler(commands=['picture'])
async def image_send(message: types.Message):
    await message.answer_photo(
        open('images/l5.jpg', 'rb')
    )
    await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.answer(message.text.upper())
    else:
        await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp)



