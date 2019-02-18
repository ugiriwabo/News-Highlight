from app import app
import urllib.request,json
from .models import new

Source= new.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the new base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['sources']:
           new_results_list = get_news_response['sources']
           new_results = process_results(new_results_list)


    return new_results

def process_results(new_list):
    '''
    Function  that processes the new result and transform them to a list of Objects

    Args:
       new_list: A list of dictionaries that contain new details

    Returns :
        new_results: A list of new objects
    '''
    new_results = []
    for new_item in new_list:
        id = new_item.get('id')
        title = new_item.get('original_title')
        overview = new_item.get('overview')
        poster = new_item.get('poster_path')
        vote_average = new_item.get('vote_average')
        vote_count = new_item.get('vote_count')

        if poster:
            new_object = new(id,title,overview,poster,vote_average,vote_count)
            new_results.append(new_object)

    return new_results





