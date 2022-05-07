import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from random import randrange

bot = Bot(token="5111560786:AAGQImq62wzJPza68i5jsFzDnxQLSeYMXnk")
dp = Dispatcher(bot)

btnDice = KeyboardButton("/dice")
btnTimer = KeyboardButton("/timer")
menuStart = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDice, btnTimer)
btnOneDie = KeyboardButton("кинуть один шестигранный кубик")
btnTwoDie = KeyboardButton("кинуть 2 шестигранных кубика одновременно")
btnBigDie = KeyboardButton("кинуть 20-гранный кубик")
btnReturn = KeyboardButton("вернуться назад")
menuDice = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(btnOneDie, btnTwoDie, btnBigDie, btnReturn)
btnHalfMinute = KeyboardButton("30 секунд")
btnOneMinute = KeyboardButton("1 минута")
btnFiveMinute = KeyboardButton("5 минут")
menuTimer = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(btnHalfMinute, btnOneMinute,
                                                                       btnFiveMinute, btnReturn)
btnClose = KeyboardButton("/close")
menuClose = ReplyKeyboardMarkup(resize_keyboard=True).add(btnClose)
que = {}


async def timer(user, time, msg):
    await bot.send_message(user, f"Засёк {msg}", reply_markup=menuClose)
    que[user] = time
    for i in range(time):
        if user not in que:
            await bot.send_message(user, "вы успешно сбросили таймер", reply_markup=menuTimer)
            break
        await asyncio.sleep(1)
    if user in que:
        await bot.send_message(user, f"{msg} истекло", reply_markup=menuTimer)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("старт",  reply_markup=menuStart)


@dp.message_handler(commands=["dice"])
async def help_command(message: types.Message):
    await message.reply("дайс", reply_markup=menuDice)


@dp.message_handler(commands=["timer"])
async def help_command(message: types.Message):
    await message.reply("таймер", reply_markup=menuTimer)


@dp.message_handler(commands=["close"])
async def help_command(message: types.Message):
    del que[message.from_user.id]


@dp.message_handler()
async def main(message: types.Message):
    msg = message.text
    if msg == "вернуться назад":
        await message.reply("вы вернулись назад", reply_markup=menuStart)
    elif msg == "кинуть один шестигранный кубик":
        await message.reply(f"{randrange(1, 6)}")
    elif msg == "кинуть 2 шестигранных кубика одновременно":
        await message.reply(f"{randrange(1, 6)}, {randrange(1, 6)}")
    elif msg == "кинуть 20-гранный кубик":
        await message.reply(f"{randrange(1, 20)}")
    elif msg == "30 секунд":
        await timer(message.from_user.id, 30, msg)
    elif msg == "1 минута":
        await timer(message.from_user.id, 60, msg)
    elif msg == "5 минут":
        await timer(message.from_user.id, 300, msg)


if __name__ == '__main__':
    executor.start_polling(dp)
