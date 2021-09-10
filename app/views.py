from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    Root page function that returns the index page and its data
    '''
    message = 'Hello Moses!!'
    return render_template('index.html',  message= message)

@app.route('/articles/<article_id>')
def movie(article_id):

    '''
    View article page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = article_id)