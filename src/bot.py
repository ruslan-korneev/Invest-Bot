import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


# Configure logging
logging.basicConfig(
        filename='bot.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S')

# Telegram token from Bot Father
TG_TOKEN = os.environ.get('TG_TOKEN')

# Initialize bot and dispatcher
bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Form(StatesGroup):
    """ Fields for tasks """
    stock = State()
    country = State()
    period = State()


# Start with hello message
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    reply = """
    Привет!
    Бот для помощи в Инвестициях и Трейдинге
    """
    await message.reply(reply)


@dp.message_handler(commands=['get_graph_last_month'])
async def get_graph_last_month(message: types.Message):
    reply = """
    send me stock, for example of Apple:
        AAPL
    """
    await message.reply(reply)
    await Form.stock.set()


@dp.message_handler(state=Form.stock)
async def process_add_stock(message: types.Message, state: FSMContext):
    """
        Process for adding stock
    """
    async with state.proxy() as state_data:
        state_data['stock'] = message.text
    await message.answer(
        'Пришлите страну компании')
    await Form.country.set()


@dp.message_handler(state=Form.country)
async def process_add_country(message: types.Message, state: FSMContext):
    """
        Process for adding country
    """
    async with state.proxy() as state_data:
        state_data['country'] = message.text
    await message.answer(
        f"Отлично\n{state_data['stock']}\n{state_data['country']}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
