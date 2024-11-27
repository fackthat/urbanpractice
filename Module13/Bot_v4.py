from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text= 'Рассчитать')
button2 = KeyboardButton(text= 'Информация')
keyboard.add(button1)
keyboard.add(button2)

@dp.message_handler(commands="start")
async def start(message):
    await message.answer("Привет! Выберите действие:", reply_markup=keyboard)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(filters.Text(equals='Информация', ignore_case=True))
async def info(message):
    await message.answer("Этот бот помогает рассчитать норму калорий на основе ваших параметров.")

@dp.message_handler(filters.Text(equals='Рассчитать', ignore_case=True))
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

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
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Введи слово "Calories", чтобы узнай свою норму потребления калорий в день')

# @dp.message_handler()
# async def all_message(message):
#     print('Мы получили сообщение!')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)