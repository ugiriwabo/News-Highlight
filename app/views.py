from flask import render_template
from app import app
from .request import get_source ,get_alticle

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting general source
    general_news = get_source('general')
    print(general_news)
    business_news = get_source('business')
    technology_news = get_source('technology')
    sports_news = get_source('sports')
    entertainment_news = get_source('entertainment')
    science_new = get_source('science')
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title,general = general_news,business = business_news , technology = technology_news ,sports = sports_news , entertainment = entertainment_news , science = science_new)

@app.route('/new/<new_name>')
def new(new_name):

    '''
    View new page function that returns the new details page and its data
    '''
    article = get_alticle(new_name)
    title = '(new_name)'
    return render_template('new.html',title=title,articles=article)