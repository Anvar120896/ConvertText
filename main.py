import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from transliterate import to_latin, to_cyrillic


bot = Bot(token="6363094107:AAGfQavdk27FQAvhYMsR1t0YiItwruDilng")
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Salom, {(message.from_user.full_name)} \n🇷🇺-🇺🇿 \nКрилл-Lotin-Крилл botiga xush kelibsiz!")
    await message.answer(f"Matn kiriting:")


@dp.message()
async def convert(message: Message) -> None:
    await  message.answer("⏳")
    word = message.text
    if word.isascii():
        await message.reply(to_cyrillic(word))
    else:
        await message.reply(to_latin(word))



async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())