from aiogram import types, Dispatcher
from handler.constants import CURSES_TEXT
from handler.all_messages import echo

async def example(message: types.Message):
    print(f"{message.chat.type=}")
    print(f"{message.reply_to_message=}")
    print(f"{message.from_user.id=}")
    if message.chat.type != 'private':
        admins = await message.chat.get_administrators()
        print(admins)

async def check_user_is_admin(message: types.Message):
    """Проверка на админа
    """
    admins = await message.chat.get_administrators()
    for admin in admins:
        if admin["user"]["id"] == message.from_user.id:
            return True
        return False


async def check_curses(message: types.Message):
    """Удаление плохих слов из чата
    """
    BAD_WORDS = ['дурак', 'тупой', 'плохой', 'тупица', 'бля', 'сука', 'хуй', 'пидор', ]
    if message.chat.type != 'private':
        for word in BAD_WORDS:
          if message.text.lower().replace(' ', '').count(word):
            await message.answer(text=CURSES_TEXT.format(
                    first_name=message.from_user.first_name))
            message.reply_to_message, message.answer(text=f'{message.from_user}'
                                                                f' написал плохое слово! Админы предлагаю'
                                                                f' забанить его\n'
                                                                f'!да или !нет')
            await message.delete()
            break

async def pin_message(message: types.Message):
    print(message.text)
    if message.chat.type != 'private':
     admin_avtor = await check_user_is_admin(message)
     if admin_avtor and message.reply_to_message:
          await message.reply_to_message.pin()

async def ban_member(message: types.Message):
    if message.chat.type != 'private':
        admin_autor = await check_user_is_admin(message)
        print(f'{admin_autor=}')
        if admin_autor and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id)


