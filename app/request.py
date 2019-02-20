from app import app
import urllib.request,json
from .models import new 
from .models import article

Source = new.Source
Articles = article.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the new base url
base_url = app.config["NEWS_API_BASE_URL"]
base_url1=app.config["ARTICLE_API_BASE_URL"]



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


def get_alticle(source_id):
    '''
    Function that gets the json response to our url request
    '''
    get_alticle_url = base_url1.format(source_id,api_key)

    with urllib.request.urlopen(get_alticle_url) as url:
        get_alticle_data = url.read()
        get_alticle_response = json.loads(get_alticle_data)

        alticles_results = None

        if get_alticle_response['articles']:
            alticles_results_list = get_alticle_response['articles']
            alticles_results = process_result(alticles_results_list)


    return alticles_results

def process_result(alticles_list):
    '''
    Function  that processes the new alticle and transform them to a list of Objects

    Args:
        new_list: A list of dictionaries that contain new details

    Returns :
        new_alticle: A list of new objects
    '''
    alticles_results = []
    for alticle_item in alticles_list:
        id = alticle_item.get('id')
        author = alticle_item.get('author')
        title  = alticle_item.get('title ')
        description = alticle_item.get('description')
        url = alticle_item.get('url')
        urlToImage = alticle_item.get('urlToImage')
        publishedAt = alticle_item.get('publishedAt')
        content = alticle_item.get('content') 
        if urlToImage:
            news_object = Articles(id,author,title,description,url,urlToImage,publishedAt,content)
            alticles_results.append(news_object)

    return alticles_results