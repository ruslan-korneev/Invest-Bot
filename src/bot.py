import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


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


# Start with hello message
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    reply = """
    Привет!
    Бот для помощи в Инвестициях и Трейдинге
    """
    await message.reply(reply)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
