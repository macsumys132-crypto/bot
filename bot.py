import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(m: types.Message):
    await m.answer("Привіт! Напиши /free")

@dp.message(Command("free"))
async def free(m: types.Message):
    await m.answer("Ось Roblox: https://roblox.com")

@dp.message(Command("help"))
async def help_cmd(m: types.Message):
    await m.answer("Команди: /start /free /help")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
