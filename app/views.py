from flask import render_template
from app import app
from .request import get_source


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting general source
    general_news = get_source('general')
    # business_news = get_source('business')
    # technology_news = get_source('technology')
    # sports_news = get_source('sports')
    # entertainment_news = get_source('entertainment')
    # science_new = get_source('science')
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title,general = general_news)

@app.route('/new/<int:id>')
def new(id):

    '''
    View new page function that returns the new details page and its data
    '''
    new = get_source(id)
    title = f'{new.title}'

    return render_template('index.html',title = title,new = new)