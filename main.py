from email import header
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def crawl_ptt_article_content(url):
    headers = {'Cookie': 'over18=1'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    content = soup.find_all("div", {"id": "searchL"})

    for content2 in content:
        if content2.find("a", {"data-tp": "正"}):
            push_tag = content2.find("a", {"data-tp": "正"}).get_text(strip=True)
        else:
            push_tag = None
            return print('查無此字')

    URL2 = 'https://www.chinesewords.cc/character/word/' + quote(f'{push_tag[0:1]}')
    
    response2 = requests.get(URL2, headers=headers)
    soup = BeautifulSoup(response2.text, 'html.parser')

    content2 = soup.find('title').get_text()

    meta_info = soup.select('span.article-meta-value')
    if meta_info:
        for meta in meta_info: 
            content2 = content2.replace(meta.get_text(), '')

    comments = soup.find_all("div", {"class": "media-body"})
    for comment in comments:
        push_tag = comment.find("div", {"class": "kk ml-2"}).get_text(strip=True)
        # print(f'{push_tag[3:6]}')
    print(content2[0:1]+f'{push_tag[3:6]}')

search_word = input("請輸入要查詢的字: ")
article_url = 'https://dict.variants.moe.edu.tw/search.jsp?QTP=0&WORD=' + quote(search_word)
crawl_ptt_article_content(article_url)