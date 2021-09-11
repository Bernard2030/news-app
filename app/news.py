class News:
    """
    News class to define news objects
    """

    def __init__(self, id, name, url, description, country ):
        """
        Getting news objects
        """
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.country = country

class Articles:
    """
    Article class that returns details of an article
    """        
    def __init__(self,title, author,description, url, urlToImage, publishedAt, content):
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.conten = content
        

       
        