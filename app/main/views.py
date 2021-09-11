from ..request import get_news 
from flask import render_template
from . import main

#Views
@main.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    #get current news
    current_news = get_news()
    print(current_news)
    
    title = "Welcome to the Best News Website for latest and current news"
    return render_template('index.html', title= title, current = current_news )
     

@main.route("/news/<int:news_id>")
def news(source_id):
    """
    view news page function that returns the news detail page and its data from a source
    """
    #get news based on source id

    news = get_news(source_id)
    print(news)
    id = f'{source_id}'

    return render_template("news.html", new = news, id = source_id)


# @main.route('/search/<news_name>')
# def search(news_name):
#     '''
#     View function to display the search results
#     '''
#     news_name_list = news_name.split(" ")
#     news_name_format = "+".join(news_name_list)
#     searched_news = search_news(news_name_format)
#     title = f'search results for {news_name}'
#     return render_template('search.html',news = searched_news)    