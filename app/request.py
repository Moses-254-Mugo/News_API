import urllib.request, json
# from .models import Article, Source
import requests
from decouple import config
from requests.models import Response

API_KEY =config('NEWS_API_KEY')

BASE_URL =f'https://newsapi.org/v2/sources?q=Apple&from=2021-09-11&sortBy=popularity&apiKey={API_KEY}'
BASE_URL2 =f'https://newsapi.org/v2/everything?q=Apple&from=2021-09-11&sortBy=popularity&apiKey={API_KEY}'


def get_news():
    source = []
    response = requests.get(BASE_URL)
    print(response)
    if response.status_code == 200:
        for data in response.json()['sources']:
            source.append(data)

        print(source)
        return source
#
def get_articles():
    article = []
    response = requests.get(BASE_URL2)
    print(response)
    if response.status_code == 200:
        for data in response.json()['articles']:
            article.append(data)

        print(article)
        return article
