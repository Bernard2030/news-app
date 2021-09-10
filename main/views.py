from .request import get_news
from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    #get current news
    current_news = get_news()
    print(current_news)
    
    message = "Welcome to the Best News Website for latest and current news"
    return render_template('index.html', message = message, current = current_news )
     

@app.route("/news/<int:news_id>")
def news(news_id):
    """
    view news page function that returns the news detail page and its data
    """
    return render_template("news.html", id = news_id)