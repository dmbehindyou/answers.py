import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="5111560786:AAGQImq62wzJPza68i5jsFzDnxQLSeYMXnk")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply("Я пока не умею помогать... Я только ваше эхо.")


@dp.message_handler(commands=["time"])
async def help_command(message: types.Message):
    await message.reply(time.asctime().split()[3])


@dp.message_handler(commands=["date"])
async def help_command(message: types.Message):
    await message.reply(" ".join(time.asctime().split()[1:3]) + " " + time.asctime().split()[4])


if __name__ == '__main__':
    executor.start_polling(dp)
