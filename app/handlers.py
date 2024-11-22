from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from telegraph import Telegraph, upload
import random

router = Router()

class Tg(StatesGroup):
    url = State()
    article = State()
    author = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, это MStealerBot, оптравь ссылку на главу.')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Разработчики: Владимир и Станислав.\nЕсли хочешь работать дальше - нажми /start.')

@router.message(Command('pikmi'))
async def pikmi_one(message: Message, state: FSMContext):
    await state.set_state(Tg.url)
    await message.answer('Введите ссылку на главу')

@router.message(Tg.url)
async def reg_two(message:Message, state: FSMContext):
    await state.update_data(url = message.text)
    await state.set_state(Tg.article)
    await message.answer('Введите название статьи')
    
@router.message(Tg.article)
async def reg_three(message:Message, state: FSMContext):
    await state.update_data(article = message.text)
    await state.set_state(Tg.author)
    await message.answer('Введите имя автора статьи')

    #добавить обработчик надо!

@router.message(Tg.author)
async def reg_four(message:Message, state: FSMContext):
    await state.update_data(author = message.text)
    data = await state.get_data()
    await message.answer('Секундочку...')
    article = data["article"]
    author = data["author"]
    telegraph = Telegraph()
    telegraph.create_account(article, author_name=author)
    def post(title, content):
        response = telegraph.create_page(article, author_name=author, html_content = content)
        return 'https://telegra.ph/{}'.format(response['path'])
    postlink = post(article, f'<img src = {data["url"]}>')
    await message.answer (postlink)
    await state.clear()