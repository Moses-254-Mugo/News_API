import requests
from app.models import Source
from flask import render_template, request
# from ..request import get_sources, get_articles
from . import mose
from ..request import get_news,get_articles

# Views
@mose.route('/')
def index():

    '''
    Root page function that returns the index page and its data
    '''
    source = get_news()
    

    return render_template('index.html', source = source)

@mose.route('/articles')
def article_():

    '''
    View article page function that returns the article details page and its data
    '''
    article =  get_articles()
    return render_template('articles.html', article = article)