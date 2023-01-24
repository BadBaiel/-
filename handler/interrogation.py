from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


class Form(StatesGroup):
    name = State()
    age = State()
    address = State()
    day = State()
    done = State()


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply(
        'Отменено.',
        reply_markup=types.ReplyKeyboardRemove())


async def form_start(cb: types.CallbackQuery):
    """
    Стартуем наш FSM, задаем первый вопрос
    """
    await Form.name.set()
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="-------------------------------\n"
             "Введите ваше имя\n"
             "-------------------------------")



async def process_name(message: types.Message, state: FSMContext):
    """
    Обрабатываем имя, задаем второй вопрос
    """
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)

    await Form.next()
    await message.reply("------------------------------------\n"
                        "Введите ваш возраст\n"
                        "------------------------------------")


async def process_age(message: types.Message, state: FSMContext):
    """
    Обрабатывваем возраст, задаем следующий вопрос
    """
    if not message.text.isdigit():
        await message.reply("Введите ваш возраст(число)")
    else:
        async with state.proxy() as data:


            data['age']=int(message.text)

    async with state.proxy() as data:
        data['age'] = message.text
        week_days_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        week_days_kb.add(
            KeyboardButton("Понедельник"),
            KeyboardButton("Вторник"),
            KeyboardButton("Среда"),
            KeyboardButton("Четверг"),
            KeyboardButton("Пятница")
        )
    await Form.next()
    await message.reply(
        "Выберите день недели для получения посылки в ближайшую неделю",
        reply_markup=week_days_kb
    )
async def process_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
        print(data)
    await Form.next()
    await message.reply("---------------------------------\n"
                        "Введите ваш aдрес\n"
                        "---------------------------------")



async def process_day(message: types.Message, state: FSMContext):
    """
    Обрабатываем введенный день недели, задаем следующий вопрос
    """
    async with state.proxy() as data:
        data['day']=message.text

    yes_no_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_no_kb.add(
        KeyboardButton("Да"),
        KeyboardButton("Нет")
    )

    await Form.next()
    await message.reply(f"""Подтвердите ваши данные:
    Имя: {data['name']}
    Возраст: {data['age']}
    Адрес: {data['day']}
    День, когда вы можете получить посылку: {data['address']}
    Данные верны?
    """, reply_markup=yes_no_kb)
    if message.from_user == 'нет':
        print('Можете пройти опрос заново')
    else:
        print()

async def process_done(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(
        "Спасибо. Мы с вами свяжемся.",
        reply_markup=ReplyKeyboardRemove()

    )