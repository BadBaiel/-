from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from handler.start import start_command
from handler.help import help_command
from handler.pictures import image_sender
from handler.interrogation import Form, process_name, form_start, process_age, process_address,process_day, process_done
from handler.shop import shop_start
from handler.shop import addres
from handler.Admin import example, check_user_is_admin, check_curses, pin_message, ban_member
from handler.shop_categories import show_gun, show_weapon, show_semiautomatic_weapon
from handler.prikol import check_cur
from handler.all_messages import echo

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(getenv('TG_TOKEN'))
    dp = Dispatcher(bot, storage=MemoryStorage())

    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(help_command, commands=["help"])
    dp.register_message_handler(image_sender, commands=["picture"])
    dp.register_callback_query_handler(form_start, text="form")
    dp.register_callback_query_handler(shop_start, text='shop_start')
    dp.register_callback_query_handler(addres, text='addres')
    dp.register_message_handler(show_gun, Text(equals='Хочу пистолет'))
    dp.register_message_handler(show_weapon, Text(equals='Хочу автомат'))
    dp.register_message_handler(show_semiautomatic_weapon, Text(equals='Хочу полуавтомат'))
    # dp.register_message_handler(echo)
    dp.register_message_handler(check_cur)
    dp.register_message_handler(check_curses)
    dp.register_message_handler(ban_member, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(process_name, state=Form.name)
    dp.register_message_handler(process_age, state=Form.age)
    dp.register_message_handler(process_address, state=Form.address)
    dp.register_message_handler(process_day, state=Form.day)
    dp.register_message_handler(process_done, state=Form.done)
    dp.register_message_handler(example)
    dp.register_message_handler(check_user_is_admin)

    executor.start_polling(dp, skip_updates=True)