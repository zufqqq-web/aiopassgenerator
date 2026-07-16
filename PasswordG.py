import asyncio
import secrets
import string
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "YOUR_TOKEN"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("Используй: /pass <длина>\nПример: /pass 16 (по умолчанию 12)")

@dp.message(Command("pass"))
async def gen_password(msg: types.Message):
    args = msg.text.split()
    length = 12
    if len(args) > 1 and args[1].isdigit():
        length = min(int(args[1]), 64) # Макс 64 символа

    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    await msg.answer(f"Твой пароль:\n`{password}`", parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())