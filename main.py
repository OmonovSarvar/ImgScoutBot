import config
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message

bot = Bot(token='7838660808:AAEbJI8tqZ5EP6x0NkxSHNnzJ5McMm9C5J4')
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_handler(message: Message):
    await message.reply(message.text)


async def on_startup():
    await dp.start_polling()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
