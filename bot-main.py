from aiogram.utils import executor
from bot_create import dp
import asyncio
from handlers import naked, applicants, companies, forchannel

async def on_startup(_):
    print('Бот вышел в онлайн')

naked.register_handlers_client(dp)
applicants.register_handlers_client(dp)
companies.register_handlers_client(dp)
forchannel.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
