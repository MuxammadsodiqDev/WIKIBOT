import asyncio
import logging
import sys
import wikipedia

from aiogram import Bot, Dispatcher, html, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

#this is bot token
BOT_TOKEN = "7381610188:AAHqQkYr1GXsIbe3FmY6fr3hiuBxF0KBDH8"
TOKEN = BOT_TOKEN
wikipedia.set_lang('uz')

router = Router()
dp = Dispatcher()

#router Add dispatcher
dp.include_router(router)

#this is start command
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f" Assalomu alaykum, {html.bold(message.from_user.full_name)}\nWIKIBOTdan hohlaganingizni so'rang!!!")

#this is privacy command
@router.message(Command(commands=["privacy"]))
async def privacy(message: Message):
    await message.answer(f"Quyidagi link ustiga bosing: [privacy link](https://docs.google.com/document/d/1KI_BSOVnu7YMB_sWzFDXq4rPM8syp3s3-B4joOazVmo/edit?usp=sharing)",parse_mode="Markdown")

#this is wiki handler
@router.message()
async def sendwiki(message: Message) -> None:
    try:
        respound = wikipedia.summary(message.text)
        await message.answer(respound)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())    
