
import urllib.request, json
from app.models import News, Articles




#Getting api key
api_key = None

#Getting the news base url
base_url = None
#getting get_article base url
base_url_get_article = None

def configure_request(app):
    global api_key,base_url, articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_base_url = app.config['ARTICLES_BASE_URL']

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
       category = news_item.get('category')
       country = news_item.get('country')
       

       if name:
                news_object = News(id, name,  description, url, category, country )
                news_results.append(news_object) 



    return news_results 

def get_articles(id):
    """
    Function that gets the json response for our url request
    """  
    #   
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=e984567f65124d82bdb23cfc40ce31b8'.format(id)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results 

def process_articles(articles_list):
    """
    A function that processes the news result and transform them to a list of objects

    Args:
        articles_list: A list of dictionary that returns news details

    return:
         articles_results: A list of news objects    
    """           
    articles_results = []
    for articles_item in articles_list:
       title =  articles_item.get('title')
       author =  articles_item.get('author')
       description =  articles_item.get('description')
       url =  articles_item.get('url')
       urlToImage =  articles_item.get('urlToImage')
       publishedAt =  articles_item.get('publishedAt')
       content =  articles_item.get('content')
       

       if urlToImage:
            articles_object = Articles(
                    title, author, description, url,       urlToImage, publishedAt, content )
            articles_results.append(articles_object)
                
             
    
            


    return  articles_results 


# def search_news(news_name):
#     search_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'.format(api_key,news_name)
#     with urllib.request.urlopen(search_news_url) as url:
#         search_news_data = url.read()
#         search_news_response = json.loads(search_news_data)

#         search_news_results = None

#         if search_news_response['sources']:
#             search_news_list = search_news_response['sources']
#             search_news_results = process_results(search_news_list)


#     return search_news_results 


