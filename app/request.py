from app import app
import urllib.request,json
from .models import new

Source = new.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the new base url
base_url = app.config["NEWS_API_BASE_URL"]



def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        sources_results = None

        if get_source_response['sources']:
            sources_results_list = get_source_response['sources']
            sources_results = process_results(sources_results_list)


    return sources_results

def process_results(sources_list):
    '''
    Function  that processes the new source and transform them to a list of Objects

    Args:
        new_list: A list of dictionaries that contain new details

    Returns :
        new_sources: A list of new objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if category:
            news_object = Source(id,name,description,url,category,language,country)
            sources_results.append(news_object)

    return sources_results
