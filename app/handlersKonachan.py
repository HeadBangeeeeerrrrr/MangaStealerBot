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

del_keyb = ReplyKeyboardRemove()

keyboard0 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "··•••Начать•••··")]], resize_keyboard=True)

keyboard1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "Сбор картинок")], [KeyboardButton(text = "Стоп")]], resize_keyboard=True)

keyboard2 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "Назад")]], resize_keyboard=True)

keyboard3 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "Продолжить")], [KeyboardButton(text = "Стоп")]], resize_keyboard=True)

@router.message(CommandStart())
async def nachat_cmd(message: Message):
    await message.answer("Тебя приветствует picSteal бот, жми кнопку, чтобы начать", reply_markup=keyboard0)

@router.message(F.text == "··•••Начать•••··")
async def konachan_cmd(message: Message, state: FSMContext):
    await message.answer("Выберите действие: ", reply_markup=keyboard1)

@router.message(F.text == "Назад")
async def back_to_site_choice(message: Message, state: FSMContext):
    await state.set_state()  
    await konachan_cmd(message, state)

@router.message(F.text == "Продолжить")
async def returning(message: Message, state: FSMContext):
    await state.set_state()  
    await konachan_cmd(message, state)
    
@router.message(F.text == "Отмена")
async def cancel(message: Message, state: FSMContext):
    await state.set_state()  
    await konachan_cmd(message, state)

@router.message(F.text == "Сбор картинок")
async def sbor_pics(message: Message, state: FSMContext):
    await state.set_state(Tg.url)
    await message.answer('Введите ссылку на страницу: ', reply_markup=keyboard2)

    @router.message(Tg.url)
    async def main_reg_one(message:Message, state: FSMContext):
        if message.text.startswith("https://konachan"):
            await state.update_data(url=message.text)  
            await state.set_state(Tg.page)
            await message.answer('Введите количество страниц, которое нужно обработать: ')
            await message.answer('Учтите: чем больше страниц нужно обработать, тем больше времени боту придется на это затратить')
        else:
            await message.answer("Некорректно введена ссылка, попробуйте еще раз.")
    @router.message(Tg.page)
    async def main_reg_two(message:Message, state: FSMContext):
        await state.update_data(page = message.text)
        if (message.text.isdigit()):
            if (int(message.text) > 0):
                await state.update_data(page = int(message.text))
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
                first = int(match.group(1)) if match else None

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
                    try:
                        await message.answer_media_group(media=media)
                        await asyncio.sleep(1.5)
                    except Exception as e:
                        await asyncio.sleep(5)
                await state.clear()
                await message.answer("Готово!", reply_markup=keyboard0)
                await message.answer("Если бот вам больше не нужен, нажмите на команду 'стоп'", reply_markup=keyboard3)
        else:
            await message.answer("Некорректный ввод. Пожалуйста, введите число без букв и символов.")
            await message.answer('Введите количество страниц, которое нужно обработать: ')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Данный бот разработан с целью парсинга (сбора) картинок с сайта: \n╭─────────ᘒ─────────╮\n         https://konachan.net/ \n╰─────────ᘒ─────────╯', disable_web_page_preview=True)
    await message.answer('Все работает до безобразия просто: \n     Шаг 1: необходимо зайти на сайт и скопировать URL (ссылку) страницы, с которой нужно взять картинки.\n      Шаг 2: отправить в чат боту команду /start\n      Шаг 3: следовать указаниям бота.\n')
    #await message.answer('Примечания по работе бота: \n    •Из сайта https://e-shuushuu.net/ картинки весм больше 5мб скачаны не будут. Это связано с тем, что телеграм попросту не умеет принимать картинку размером более 5мб.\n', disable_web_page_preview=True)
    await message.answer('Разработчик: Станислав.\nДля дальнейшей работы с ботом нажми /start')

@router.message(F.text == 'Стоп' or Command('stop'))
async def stop_bot(message: Message):
    await message.answer("Бот отключен. Клавиатура удалена.", reply_markup=ReplyKeyboardRemove())