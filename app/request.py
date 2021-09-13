import urllib.request, json
from app.models import Article, Source

# from decouple import config
# from request.models import Response

api_key = None

base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_URL']




def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=ff155ef8eb334dfaa680f9807dc1582e'
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_sources = None
        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_results(news_sources_list)
    return news_sources

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    Articles_sources = []
    for new_item in news_list:
        id = new_item.get('id')
        name = new_item.get('name')
        url = new_item.get('url')
        description = new_item.get('description')
        title = new_item.get('title')
        author = new_item.get('author')
        urlToImage = new_item.get('urlToImage')
        content = new_item.get('content')
        publishedAt = new_item.get('publishedAt')

        
        if id:
            news_object = Article(id,name,url,description,title,author,urlToImage,content, publishedAt)
            Articles_sources.append(news_object)
    return Articles_sources



def get_new_source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey==ff155ef8eb334dfaa680f9807dc1582e'.format()
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        news_sources = None
        if get_source_response['articles']:
            news_sources_list = get_source_response['articles']
            news_sources = process_results(news_sources_list)
    return news_sources

def process_source_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    Articles_results = []
    for new_item in news_list:
        id = new_item.get('id')
        name = new_item.get('name')                
        description = new_item.get('description')
        url = new_item.get('url')
        country = new_item.get('country')
        language = new_item.get('language')
        if id:
            news_object = Source(id,name,description,url,language,country)
            Articles_results.append(news_object)
    return Articles_results

