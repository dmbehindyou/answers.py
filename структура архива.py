from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

storage = MemoryStorage()
bot = Bot(token="5111560786:AAGQImq62wzJPza68i5jsFzDnxQLSeYMXnk")
dp = Dispatcher(bot, storage=storage)


class Dialog(StatesGroup):
    first_response = State()
    second_response = State()


@dp.message_handler(state="*", commands=["stop"])
async def help_command(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Всего доброго!")
    await state.finish()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await Dialog.first_response.set()
    await bot.send_message(message.from_user.id, "Привет. Пройдите небольшой опрос, пожалуйста!\n"
                           "Вы можете прервать опрос, послав команду /stop.\n"
                           "В каком городе вы живёте?")


@dp.message_handler(state=Dialog.first_response)
async def help_command(message: types.Message, state: FSMContext):
    if message.text == "/skip":
        await bot.send_message(message.from_user.id, "Какая погода у вас за окном?")
    else:
        await bot.send_message(message.from_user.id, f"Какая погода в городе {message.text}?")
    await Dialog.next()


@dp.message_handler(state=Dialog.second_response)
async def help_command(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, f"Спасибо за участие в опросе! Всего доброго!")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp)
