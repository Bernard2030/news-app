from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    message = "I love Dorcas so much and I don't Know Why??"
    return render_template('index.html', message = message)

@app.route("/news/<int:news_id>")
def news(news_id):
    """
    view news page function that returns the news detail page and its data
    """
    return render_template("news.html", id = news_id)