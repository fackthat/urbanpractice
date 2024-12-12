import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters

from config import *
from keyboards import *
import texts
from crud_functions import initiate_db, get_all_products, add_user, is_uncluded

initiate_db()
logging.basicConfig(level=logging.INFO)
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())


@dp.message_handler(commands='start')
async def start(message):
    await message.answer(f'Привет, {message.from_user.username}! ' + texts.choose, reply_markup=keyboard)


@dp.message_handler(filters.Text(equals='Рассчитать', ignore_case=True))
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

@dp.message_handler(filters.Text(equals='Купить', ignore_case=True))
async def get_buying_list(message):
    products = get_all_products()

    if not products:
        await message.answer("Продуктовая база пуста")
    for product in products:
        product_text = (
            f"Название: {product[1]} | "
            f"Описание: {product[2]} | "
            f"Цена: {product[3]}₽"
        )
        try:
            with open(f"files/{product[1].replace(' ', '_')}.jpg", 'rb') as photo:
                await message.answer_photo(photo, caption=product_text)
        except FileNotFoundError:
            await message.answer(product_text)
    await message.answer('Выберите продукт для покупки:', reply_markup=products_keyboard)


@dp.callback_query_handler(filters.Text(equals="product_buying"))
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()



@dp.callback_query_handler(filters.Text(equals='formulas'))
async def get_formulas(call):
    await call.message.answer(texts.formula_text)
    await call.answer()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.message_handler(filters.Text(equals='Регистрация', ignore_case=True))
async def sign_up(message):
    await message.answer(texts.registration, reply_markup=keyboard)
    await RegistrationState.username.set()

@dp.message_handler(state = RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if is_uncluded(username):
        await message.answer(f'Пользователь уже существует, введите другое имя:')
    else:
        await state.update_data(username=username)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@dp.message_handler(state = RegistrationState.email)
async def set_email(message, state):
    email = message.text
    await state.update_data(email=email)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state = RegistrationState.age)
async def set_age(message, state):
    try:
        age = int(message.text)
        user_data = await state.get_data()
        add_user(user_data['username'], user_data['email'], age)
        await message.answer('Регистрация прошла успешно!')
        await state.finish()
    except ValueError:
        await message.answer('Введите корректный возраст (число):')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(filters.Text(equals='Информация', ignore_case=True))
async def info(message):
    await message.answer(texts.info, reply_markup=keyboard)

@dp.callback_query_handler(filters.Text(equals='calories'))
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def set_calories(message, state):
    await state.update_data(weight = int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Ваша норма калорий: {calories:.2f} ккал в день')
    await state.finish()


# @dp.message_handler(commands=['start'])
# async def start_message(message):
#     print('start message')

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.welcome, reply_markup=keyboard)

# @dp.message_handler()
# async def all_message(message):
#     print('Мы получили сообщение!')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
