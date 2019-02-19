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
    # print(general_news)
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title,general = general_news)
