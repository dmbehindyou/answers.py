from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

storage = MemoryStorage()
bot = Bot(token="5111560786:AAGQImq62wzJPza68i5jsFzDnxQLSeYMXnk")
dp = Dispatcher(bot, storage=storage)


class Dialog(StatesGroup):
    come = State()
    first_room = State()
    second_room = State()
    third_room = State()
    fourth_room = State()
    exit_state = State()


@dp.message_handler(state="*", commands=["stop"])
async def help_command(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Всего доброго!")
    await state.finish()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Здравствуйте, вы можете войти в музей по команде /войти")


@dp.message_handler(commands=["войти"])
async def start_command(message: types.Message):
    await Dialog.first_room.set()
    await bot.send_message(message.from_user.id, "Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!")


@dp.message_handler(state=Dialog.first_room)
async def first(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Вы можете перейти в комнату 2 по команде /2"
                                                 " или выйти по команде /выйти")
    await Dialog.next()


@dp.message_handler(state=Dialog.second_room)
async def second(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!")
    await Dialog.next()


@dp.message_handler(state=Dialog.third_room)
async def third(message: types.Message, state: FSMContext):
    await Dialog.next()


@dp.message_handler(state=Dialog.fourth_room)
async def fourth(message: types.Message, state: FSMContext):
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp)
