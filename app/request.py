
from app import app
import urllib.request, json
from .models import news

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news():
    """
    Function that gets the json response to our url request
    """
    get_news_url ='https://newsapi.org/v2/top-headlines/sources?apiKey=e984567f65124d82bdb23cfc40ce31b8'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results 

def process_results(news_list):
    """
    A function that processes the news result and transform them to a list of objects

    Args:
        news_list: A list of dictionary that returns news details

    return:
         news_results: A list of news objects    
    """           
    news_results = []
    for news_item in news_list:
       id = news_item.get('id')
       name = news_item.get('name')
       description = news_item.get('description')
       url = news_item.get('url')
       

    if name:
            new_object = News(name, id, description, url )
            news_results.append(new_object) 



    return news_results    