
import urllib.request, json
from app.models import News, Articles



#Getting api key
api_key = None

#Getting the news base url
base_url = None
#getting get_article base url
base_url_get_article = None

def configure_request(app):
    global api_key,base_url, base_url_get_article
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
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

def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['sources']:
            search_news_list = search_news_response['sources']
            search_news_results = process_results(search_news_list)


    return search_news_results       

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
       category = news_item.get('category')
       country = news_item.get('country')
       

    if name:
            news_object = News(name, id, description, url, category, country )
            news_results.append(news_object) 



    return news_results 

def get_articles(articles):
    """
    Function that gets the json response for article url
    """    
    get_articles_url = 'https://newsapi.org/v2/everything?q={}&from=2021-09-11&sortBy=popularity&apiKey=e984567f65124d82bdb23cfc40ce31b8'.format(articles)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        get_articles = None

        if get_articles_response['articles']:
            get_articles_list = get_articles_response['articles']
            get_articles = process_articles(get_articles_list)

    return get_articles 

def process_articles(news_list):
    """
    A function that processes the news result and transform them to a list of objects

    Args:
        news_list: A list of dictionary that returns news details

    return:
         news_results: A list of news objects    
    """           
    news_results = []
    for news_item in news_list:
       title = news_item.get('title')
       author = news_item.get('author')
       description = news_item.get('description')
       url = news_item.get('url')
       urlToImage = news_item.get('urlToImage')
       publishedAt = news_item.get('publishedAt')
       content = news_item.get('content')
       

    if title:
            articles_object = Articles(title, author, description, url, urlToImage, publishedAt, content )
            news_results.append(articles_object)
            



    return news_results 


