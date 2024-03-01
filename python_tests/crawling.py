import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def word_preprocess(word):
    word = re.sub(r'[^\w\s]', '', word)
    word = word.lower()
    stop_words = ['a', 'an', 'the', 'in', 'with', 'to', 'for', 'from', 'of', 'at', 'on',
                  'until', 'by', 'and', 'but', 'is', 'are', 'was', 'were', 'it', 'that', 'this',
                  'my', 'his', 'her', 'our', 'as', 'not', 'has', 'it', 'for']
    if word in stop_words:
        return ''
    word = re.sub(r'\b\d+\b', '', word)
    return word

word_count = Counter()

url = 'https://www.cnn.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

news_links = []

for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.startswith('/2024/02/26') and href not in news_links:
        news_links.append(href)
print("news_links"+str(news_links))
print("size"+str(len(news_links)))

# 각 뉴스 페이지에서 본문 추출
for news_link in news_links:
    full_link = f'https://www.cnn.com{news_link}'
    response = requests.get(full_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(full_link)

    article_content = soup.select_one('div.article__content-container > div.article__content')
    if article_content:
        paragraphs = article_content.find_all('p')
        for paragraph in paragraphs:
            line = paragraph.text.strip()
            for word in line.split():
                cleaned_word = word_preprocess(word)
                if cleaned_word:
                    word_count[cleaned_word] += 1

# 단어 및 개수 출력
for word, count in word_count.items():
    print(f"{word}: {count}")