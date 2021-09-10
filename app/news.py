class News:
    """
    News class to define news objects
    """

    def __init__(self, id, name, url, description ):
        """
        Getting news objects
        """
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        

        #keyward e.g article containing ward 'amazone'
        #Date published e.g articles published yesterdayt
        #source name e.g find articles by moringa
        #domain_name e.g articles published on ktn.com
        #language e.g articles in english
        