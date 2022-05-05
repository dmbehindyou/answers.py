from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="5111560786:AAGQImq62wzJPza68i5jsFzDnxQLSeYMXnk")
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"Я получил сообщение <{message.text}>")


if __name__ == '__main__':
    executor.start_polling(dp)
