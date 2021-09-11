from app import app
import urllib.request, json
from .models import article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_sources(self):
    sources = []
    sources_url = 'https://newsapi.org/v2/sources?q={}&apiKey={}'
    response = requests.get(sources_url)
    if response.status_code == 200:
        for data in response.json()['sources']:
            sources.append(data)
            print(sources)
            return sources

def get_articles(self, article):
    article = []
    article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    response = request.get(article_url)
    if response.status_code == 200



def get_article(category):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['results']:
            article_results_list = get_article_response['results']
            article_results = process_results(article_results_list)


    return article_results