from aiogram import types, Bot
import this

import asyncio
import aioschedule

async def adaf(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer(text='OK')

async def notification():
    bot = Bot
    await bot.send_message(chat_id = chat_id, text='notify_what')

async def schedul():
    aioschedule.every(20).second.do(notification)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
