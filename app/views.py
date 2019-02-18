from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting general news
    general_news = get_news('general')
    print(general_news)
    language = get_news('en')
    country = get_news('us')
    title = 'Home - Welcome to The best new Review Website Online'
    return render_template('index.html', title = title ,general = general_news ,language = language, country = country)

@app.route('/new/<int:new_id>')
def new(new_id):

    '''
    View new page function that returns the new details page and its data
    '''
    return render_template('new.html',id = new_id)

    from .request import get_news


    