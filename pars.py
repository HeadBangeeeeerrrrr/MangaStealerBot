# import requests
# from bs4 import BeautifulSoup

# url = "https://joyreactor.com/tag/anime/33929"
# payload = {}
# headers = {
#   'sec-ch-ua-platform': '"Windows"',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#   'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
#   'sec-ch-ua-mobile': '?0'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# html_content = response.text

# with open("text.txt", "a", encoding='utf-8') as file:
#   soup = BeautifulSoup(html_content, 'html.parser')
#   file.write(soup.prettify())
# print(soup.prettify())

# import requests
# from bs4 import BeautifulSoup

# from telegraph import Telegraph, upload
# import random

# article = 'Trying'
# author = 'Stanislove'

# telegraph = Telegraph()
# telegraph.create_account(article, author_name=author)

# def post(title, content):
#     response = telegraph.create_page(article, author_name=author, html_content = content)
#     return 'https://telegra.ph/{}'.format(response['path'])

# url = 'https://safebooru.org/index.php?page=post&s=list&tags=eva_01+'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# quotes = soup.find_all('img', class_='preview')
# img_sources = [img['src'] for img in quotes if 'src' in img.attrs]

# for src_ in img_sources:
#   postlink = post(article, f'img src = <{src_}>')
# print(postlink)






#          ПОЛУРАБОЧИЙ КОД для сайта safebooru

# import requests
# from bs4 import BeautifulSoup

# from telegraph import Telegraph, upload
# import random

# import re

# article = 'Trying'
# author = ''

# telegraph = Telegraph()
# telegraph.create_account(article, author_name=author)

# def post(title, content):
#     response = telegraph.create_page(article, author_name=author, html_content = content)
#     return 'https://telegra.ph/{}'.format(response['path'])

# url = ''

# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')
    
# a_tags = soup.find_all('a')
   
# ids = [a['id'].lstrip('p') for a in a_tags if 'id' in a.attrs]
    
# for id_value in ids:
#     print(id_value)

# img_links = ''

# with open("urldel.txt", "a", encoding='utf-8') as file:
#     for id_value in ids:
#         url = f'https://safebooru.org/index.php?page=post&s=view&id={id_value}'
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         img_tag = soup.find('img', id='image')
#         if img_tag and 'src' in img_tag.attrs:
#             img_src = img_tag['src'].strip("'")
#             #Заменяем "samples" на "images"
#             img_src = img_src.replace('samples', 'images')
#             if "sample_" in img_src:
#                 img_src = img_src.replace("sample_", "")
#             if ".jpg" in img_src:
#                 img_src = re.sub(r'\.jpg.*', '.jpg', img_src)
#             img_links += f'<img src="{img_src}"> '
#             print(img_src)
#             file.write(img_src + '\n')
# postlink = post(article, img_links )
# print(postlink)






#      РАБОЧИЙ КОД ПРОСТО ТЕЛЕГРАФ ХУЕТА дял сайта konachan

# import requests
# from bs4 import BeautifulSoup

# from telegraph import Telegraph, upload
# import random

# import re

# article = 'Trying'
# author = ''
# page = 3

# telegraph = Telegraph()
# telegraph.create_account(article, author_name=author)

# def post(title, content):
#     response = telegraph.create_page(article, author_name=author, html_content = content)
#     return 'https://telegra.ph/{}'.format(response['path'])
# url = 'https://konachan.net/post'
# content = []

# if 'post?page=' in url:
#     url = url
# elif 'post?tags=' in url:
#     url = url.replace('post?', f'post?page=1&')
# else:
#     url = url.replace('post', f'post?page=1&')

# match = re.search(r'page=(\d+)', url)
# first = int(match.group(1)) if match else None

# for pg in range(first, first+page):
#     real_url = re.sub(r'page=\d+', f'page={pg}', url)
#     response = requests.get(real_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a', class_=['directlink largeimg', 'directlink smallimg'])
#     for link in links:
#         href = link.get('href').strip()
#         content.append(href)
#         # content.append(f'<img src="{href}">')
#         print(href)
# final_content = ''.join(content)
# article_link = post(article, final_content)
# print(article_link)






# import requests
# from bs4 import BeautifulSoup

# from telegraph import Telegraph, upload
# import random

# import re

# article = 'Trying'
# author = ''
# page = 3

# telegraph = Telegraph()
# telegraph.create_account(article, author_name=author)

# def post(title, content):
#     response = telegraph.create_page(article, author_name=author, html_content = content)
#     return 'https://telegra.ph/{}'.format(response['path'])
# url = 'https://konachan.net/post?page=100'
# content = []

# if 'post?page=' in url:
#     url = url
# elif 'post?tags=' in url:
#     url = url.replace('post?', f'post?page=1&')
# else:
#     url = url.replace('post', f'post?page=1&')

# cut_url = url.split('/post')[0]

# match = re.search(r'page=(\d+)', url)
# first = int(match.group(1)) if match else None

# for pg in range(first, first+page):
#     real_url = re.sub(r'page=\d+', f'page={pg}', url)
#     response = requests.get(real_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a', class_="thumb")
#     for link in links:
#         href = link.get('href').strip()
#         img_response = requests.get(f'{cut_url}{href}')
#         img_soup = BeautifulSoup(img_response.text, 'html.parser')
#         img_tag = img_soup.find('img', class_='image', id='image')
#         if img_tag:
#             img_link = img_tag.get('src')
#             if img_link:
#                 content.append(f'<img src="{img_link}" alt="Изображение">')
#                 print(img_link)
# final_content = ''.join(content)
# article_link = post(article, final_content)
# print(article_link)



# import requests
# from bs4 import BeautifulSoup

# from telegraph import Telegraph, upload
# import random

# import re

# article = 'Trying'
# author = ''
# page = 1

# telegraph = Telegraph()
# telegraph.create_account(article, author_name=author)

# def post(title, content):
#     response = telegraph.create_page(article, author_name=author, html_content = content)
#     return 'https://telegra.ph/{}'.format(response['path'])

# url = 'https://e-shuushuu.net/search/results/?tags=3801'

# content = []

# if '?page=2' in url:
#     url = url
# elif 'search' in url:
#     url = url.replace('results/?', f'results/?page=1&')
# else:
#     url = f"{url}?page=1"

# match = re.search(r'page=(\d+)', url)
# first = int(match.group(1)) if match else None

# cut_url = 'https://e-shuushuu.net'

# content = []

# for pg in range(first, first+page):
#     real_url = re.sub(r'page=\d+', f'page={pg}', url)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a', class_='thumb_image')
#     for link in links:
#         href = link.get('href').strip()
#         response2 = requests.head(f'{cut_url}{href}')
#         size = int(response2.headers.get('Content-Length', 0))
#         size_mb = size / (1024 * 1024)  # Переводим в МБ
#         if (size_mb < 4.9):
#             content.append(f'<img src="{cut_url}{href}">')
#             print(f'{cut_url}{href} - {size_mb}')
#     final_content = ''.join(content)
#     article_link = post(article, final_content)
#     print(article_link)



# import requests
# from bs4 import BeautifulSoup

# from telegraph import Telegraph, upload
# import random

# import re

# url = 'https://konachan.net/post?page=100'
# content = []
# page = 2

# if 'post?page=' in url:
#     url = url
# elif 'post?tags=' in url:
#     url = url.replace('post?', f'post?page=1&')
# else:
#     url = url.replace('post', f'post?page=1&')

# cut_url = url.split('/post')[0]

# match = re.search(r'page=(\d+)', url)
# first = int(match.group(1)) if match else None

# for pg in range(first, first+page):
#     real_url = re.sub(r'page=\d+', f'page={pg}', url)
#     response = requests.get(real_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a', class_="thumb")
#     for link in links:
#         href = link.get('href').strip()
#         img_response = requests.get(f'{cut_url}{href}')
#         img_soup = BeautifulSoup(img_response.text, 'html.parser')
#         img_tag = img_soup.find('img', class_='image', id='image')
#         if img_tag:
#             img_link = img_tag.get('src')
#             if img_link:
#                 content.append(f'<img src="{img_link}" alt="Изображение">')
#                 print(img_link)


# import requests
# from bs4 import BeautifulSoup

# from telegraph import Telegraph, upload
# import random

# import re

# page_ = 2
# #await message.answer(page_)
# url_ = 'https://e-shuushuu.net/search/results/?tags=193'
# #await message.answer(url_)
# if '?page=' in url_:
#     url_ = url_
# elif 'search' in url_:
#     url_ = url_.replace('results/?', f'results/?page=1&')
# else:
#      url_ = f"{url_}/?page=1"

# match = re.search(r'page=(\d+)', url_)
# first = int(match.group(1)) if match else None

# #cut_url = 'https://e-shuushuu.net'
# cut_url = url_.split('/post')[0]

# content = []

# for pg in range(first, first+page_):
#     real_url = re.sub(r'page=\d+', f'page={pg}', url_)
#     response = requests.get(real_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a', class_='thumb_image')
#     for link in links:
#         href = link.get('href').strip()
#         response2 = requests.head(f'{cut_url}{href}')
#         # href = f'{cut_url}{link.get('href').strip()}'
#         # response2 = requests.head(href)
#         size = int(response2.headers.get('Content-Length', 0))
#         size_mb = size / (1024 * 1024)  # Переводим в МБ
#         if (size_mb < 4.9):
#             content.append(f'{cut_url}{href}')
#             print(f'{cut_url}{href}')        


# import requests
# from bs4 import BeautifulSoup

# from telegraph import Telegraph, upload
# import random

# import re


# url = 'https://danbooru.donmai.us/posts?page=97&tags=-nude+-underwear'
# content = []
# page = 2

# if 'posts?page=' in url:
#     url = url
# elif 'posts?tags=' in url:
#     url = url.replace('posts?', f'posts?page=1&')
# else:
#     url = url.replace('posts', f'posts?page=1&')

# cut_url = 'https://danbooru.donmai.us/'

# match = re.search(r'page=(\d+)', url)
# first = int(match.group(1)) if match else None

# for pg in range(first, first+page):
#     real_url = re.sub(r'page=\d+', f'page={pg}', url)
#     response = requests.get(real_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a', class_="post-preview-link")
#     for link in links:
#         href = link.get('href').strip()
#         img_response = requests.get(f'{cut_url}{href}')
#         img_soup = BeautifulSoup(img_response.text, 'html.parser')
#         img_tag = img_soup.find('img', class_='fit-width', id='image')
#         if img_tag:
#             img_link = img_tag.get('src')
#             if img_link:
#                 content.append(f'<img src="{img_link}" alt="Изображение">')
#                 print(img_link)