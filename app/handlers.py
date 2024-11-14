from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, это MStealerBot, оптравь ссылку на главу.')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Разработчики: реально крутые мужики.\nЕсли хочешь работать дальше - нажми /start.')