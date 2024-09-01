import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BotConfig
from utils import video_url

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(F.text.startswith('https://www.instagram.com/reel/') | F.text.startswith('https://instagram.com/reel/'))
async def echo_handler(message: Message) -> None:
    msg = await message.answer('Downloading.')
    try:
        data = await video_url(message.text)
        await message.bot.send_video(message.chat.id, data['downloadUrl'], caption=data['videoTitle'],
                                     reply_to_message_id=message.message_id)
    except TelegramBadRequest:
        await message.answer('Your video size > 20mb')
    except Exception as e:
        await message.answer(str(e))
    finally:
        await message.bot.delete_message(message.chat.id, msg.message_id)


async def main() -> None:
    bot = Bot(token=BotConfig.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
