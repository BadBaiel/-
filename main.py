from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
import logging

from handler.start import start_command
from handler.help import help_command
from handler.pictures import image_sender
from handler.shop import shop_start
from handler.shop import addres
from handler.Admin import example
from handler.shop_categories import show_gun, show_weapon, show_semiautomatic_weapon
from handler.prikol import check_curses
from handler.all_messages import echo


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(getenv('TG_TOKEN'))
    dp = Dispatcher(bot)

    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(help_command, commands=["help"])
    dp.register_message_handler(image_sender, commands=["picture"])
    dp.register_callback_query_handler(shop_start, text='shop_start')
    dp.register_callback_query_handler(addres, text='addres')
    dp.register_message_handler(show_gun, Text(equals='Хочу пистолет'))
    dp.register_message_handler(show_weapon, Text(equals='Хочу автомат'))
    dp.register_message_handler(show_semiautomatic_weapon, Text(equals='Хочу полуавтомат'))
    dp.register_message_handler(example)
    dp.register_message_handler(check_curses)
    dp.register_message_handler(echo)


    executor.start_polling(dp, skip_updates=True)
