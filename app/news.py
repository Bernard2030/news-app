class News:
    """
    News class to define news objects
    """

    def __init__(self, id, name, description, url,  category,  country, ):
        """
        Getting news objects
        """
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
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
        self.content = content
        

       
        