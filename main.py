from aiogram import Bot, Dispatcher
import asyncio
import logging
import sys
from config import BOT_TOKEN
from modules.default import router

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d:%(name)s:%(levelname)s:%(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.FileHandler("apex_bot.log", mode='w', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)  # Вывод и в консоль
    ]
)


masked_token = BOT_TOKEN[:10] + "..." if len(BOT_TOKEN) > 10 else BOT_TOKEN
logging.info("Bot Token loaded: %s", masked_token)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Exit")