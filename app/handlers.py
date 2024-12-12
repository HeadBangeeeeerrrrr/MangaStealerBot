from aiogram import F, Router, types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

import requests
from bs4 import BeautifulSoup

import re

import asyncio

router = Router()

class Tg(StatesGroup):
    url = State()
    page = State()
    action_choice = 'action_choice'


del_keyb = ReplyKeyboardRemove()

@router.message(CommandStart())
async def nachat_cmd(message: Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "Начать")]], resize_keyboard=True)
    await message.answer("Тебя приветствует picSteal бот, жми кнопку, чтобы начать", reply_markup=keyboard)

@router.message(F.text == "··•••Начать•••··")
async def konachan_cmd(message: Message, state: FSMContext):
    await state.set_state(Tg.action_choice)
    keyboard3 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "Сбор картинок"),
                                        KeyboardButton(text = "Рандомная страница")],
                                        [KeyboardButton(text = "Назад")]], resize_keyboard=True)
    await message.answer("Выберите действие на сайте:", reply_markup=keyboard3)
    await state.update_data(action_choice = message.text)


@router.message(F.text == "Назад")
async def back_to_site_choice(message: Message, state: FSMContext):
    await state.set_state()  
    await nachat_cmd(message, state)

@router.message(F.text == "Сбор картинок")
async def sbor_pics(message: Message, state: FSMContext):
    await state.set_state(Tg.url)
    await message.answer('Введите ссылку на страницу')
    @router.message(Tg.url)
    async def main_reg_one(message:Message, state: FSMContext):
        await state.update_data(url = message.text)
        await state.set_state(Tg.page)
        await message.answer('Введите количество сраниц, которое нужно обработать.', reply_markup=del_keyb)
        await message.answer('Учтите: чем больше страниц нужно обработать, тем больше времени боту придется на это затратить')
    @router.message(Tg.page)
    async def main_reg_two(message:Message, state: FSMContext):
        await state.update_data(page = message.text)
        data = await state.get_data()
        await message.answer('Подождите пожалуйста, картинки уже в пути...')
        page = int(data["page"])
        url = data["url"]
        content = []
        if 'post?page=' in url:
            url = url
        elif 'post?tags=' in url:
            url = url.replace('post?', f'post?page=1&')
        else:
            url = url.replace('post', f'post?page=1&')
        cut_url = url.split('/post')[0]

        match = re.search(r'page=(\d+)', url)
        
        first = match.group(1) if match else None

        for pg in range(int(first), int(first)+page):
            real_url = re.sub(r'page=\d+', f'page={pg}', url)
            response = requests.get(real_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', class_='thumb')
            for link in links:
                href = link.get('href').strip()
                img_response = requests.get(f'{cut_url}{href}')
                img_soup = BeautifulSoup(img_response.text, 'html.parser')
                img_tag = img_soup.find('img', class_='image', id='image')
                if img_tag:
                    img_link = img_tag.get('src')
                    if img_link:
                        content.append(f'{img_link}')
                        print(img_link)
        for i in range(0, len(content), 10):
            media = [types.InputMediaPhoto(media=link) for link in content[i:i + 10]]
            await message.answer_media_group(media=media)
        await state.clear()

@router.message(F.text == 'Рандомная страница')
async def cmd_help(message: Message, state: FSMContext):
    data = await state.get_data()
    if(data["action_choice"] == "Сбор картинок"):
        await sbor_pics(message)
    await state.set_state(Tg.page)
    await message.answer('Введите количество сраниц, которое нужно обработать.', reply_markup=del_keyb)
    @router.message(Tg.page)
    async def rand_reg_two(message:Message, state: FSMContext):
        await state.update_data(page = message.text)
        data = await state.get_data()
        await message.answer('Подождите пожалуйста, картинки уже в пути...')
        page = int(data["page"])
        url = 'https://konachan.net/post?page=1&tags=order%3Arandom'
        content = []
        cut_url = url.split('/post')[0]

        match = re.search(r'page=(\d+)', url)
        
        first = match.group(1) if match else None

        for pg in range(int(first), int(first)+page):
            real_url = re.sub(r'page=\d+', f'page={pg}', url)
            response = requests.get(real_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', class_='thumb')
            for link in links:
                href = link.get('href').strip()
                img_response = requests.get(f'{cut_url}{href}')
                img_soup = BeautifulSoup(img_response.text, 'html.parser')
                img_tag = img_soup.find('img', class_='image', id='image')
                if img_tag:
                    img_link = img_tag.get('src')
                    if img_link:
                        content.append(f'{img_link}')
                        print(img_link)
        for i in range(0, len(content), 10):
            media = [types.InputMediaPhoto(media=link) for link in content[i:i + 10]]
            await message.answer_media_group(media=media)
        await state.clear()
        await message.answer("Готово рандом")



@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Данный бот разработан с целью парсинга (сбора) картинок с двух сайтов: \n╭─────────ᘒ─────────╮\n         https://konachan.net/ \n        https://e-shuushuu.net/ \n╰─────────ᘒ─────────╯', disable_web_page_preview=True)
    await message.answer('Все работает до безобразия просто: \n     Шаг 1: необходимо зайти на любой из двух сайтов и скопировать URL (ссылку) страницы, с которой нужно взять картинки.\n      Шаг 2: отправить в чат боту команду /start\n      Шаг 3: следовать указаниям бота.\n')
    await message.answer('Примечания по работе бота: \n    •Из сайта https://e-shuushuu.net/ картинки весм больше 5мб скачаны не будут. Это связано с тем, что телеграм попросту не умеет принимать картинку размером более 5мб.\n', disable_web_page_preview=True)
    await message.answer('Разработчик: Станислав.\nДля дальнейшей работы с ботом нажми /start')