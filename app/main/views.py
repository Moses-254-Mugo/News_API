from app.models import Source
from flask import render_template, request
from ..request import get_sources, get_articles
from . import main

# Views
@main.route('/')
def index():

    '''
    Root page function that returns the index page and its data
    '''
    source = get_sources()
    

    return render_template('index.html', source)

@main.route('/article<id>')
def article_page(id):

    '''
    View article page function that returns the article details page and its data
    '''
    articles = get_articles(id)
    title= f'{id}'
    return render_template('articles.html',articles = articles, title = title)