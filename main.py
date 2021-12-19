import bs4
import requests
HEADERS = {'Cookie': '_ym_d=1629040281; _ym_uid=1629040281959119801; _ga=GA1.2.1785085828.1629040281; hl=ru; fl=ru; __gads=ID=9acd0649a4481963:T=1629040281:S=ALNI_MaIO0gcZLXv72XQiWe80H7pHCfFSQ; cto_bundle=971o6l8lMkJBZ29RSEo4anprNUM0NGpPVk1vQyUyQkt0MnJrYyUyQm90YmgzU2hkZGR5RjJsdUp3elJta1NkU2VrZCUyQm5EZUxWTFQlMkZxeWZDOVFMT2tOellLTU9uTHRFUXJ4eWFyeVZJSW9MTnpqZDJ5c0UxMWZ0TmdwejVCYzBQUG9nZVljblFsa3JlU3Q3eWhhcm5sMnB6cFd2WHFpYmx3JTNEJTNE; habr_web_home=ARTICLES_LIST_ALL; _gid=GA1.2.188835794.1639910389; _ym_isad=1; _gat=1',
           'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'same-origin',
           'Sec-Fetch-User': '?1',
           'Cache-Control': 'max-age=0',
           'If-None-Match': 'W/"27cce-0T+Oe8Z0HpMo6bodBRUabMKOod8"',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
           'sec-ch-ua-mobile': '?0'
           }

KEYWORDS = {'Дизайн', 'Мозг', 'Фото', 'Web', 'Python'}

ret = requests.get('https://habr.com/ru/all/', headers=HEADERS)
ret.raise_for_status()

text = ret.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item-link')
    hubs = set(hub.find('span').text for hub in hubs)

    data = article.find(class_='tm-article-snippet__datetime-published')
    title = article.find(class_='tm-article-snippet__title-link')
    span_title = title.find('span').text
    time_data = data.find('time').text

    if KEYWORDS & hubs:
        href = title['href']
        url = 'https://habr.com' + href
        print(f'<{time_data}> <{span_title}> <{url}>')

