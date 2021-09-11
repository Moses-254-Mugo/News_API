from app import app
import urllib.request, json
from .models import Article, Source



# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['HEAD_LINES']
    base_url = app.config['BASE_URL']


def get_sources():
    '''
    Function that gets json response to te url request
    '''
    get_sources_url = base_url.format(api_key)
    with urllib.request.urlopen(get_sources_url)as url:
        get_sources_data = url.read()
        get_source_response = json.loads(get_sources_data)

        sources_results = None

        if get_source_response['sources']:
            sources_result_list = get_source_response['sources']
            sources_results = process_results(sources_results)
        
    return sources_results

def process_results(sources_result_list):
    '''
    Function that process sources
    '''
    sources_result_list = []

    for source in sources_result_list:
        id  = source.get(id)
        name = source.get(name)
        language = source.get('language')

        if language == 'en':
            source_object = Source(id,name,language)
            sources_result_list.append(source_object)
    return sources_result_list

def get_articles():
    '''
    Function that get...
    '''
    get_articles_url = base_url.format(api_key)
    with urllib.request.urlopen(get_articles_url)as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response ['articles']:
            articles_list =  get_article_response['articles']
            articles_results = process_article(articles_list)

        return article_results 


def  process_article(article):
    '''
    '''
    articles_results =[]

    for results in article:
        id = results.get(id)
        name = results.get(name)
        url = results.get(url)
        description = results.get(description)
        title = results.get(title)
        author = results.get(author)
        urlToImage = results.get(urlToImage)
        content = results.get(content)
        publishedAt = results.get(publishedAt)

    return articles_results

        