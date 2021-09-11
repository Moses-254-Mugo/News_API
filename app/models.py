class Article:
    '''
    Article class to define Article object
    '''
    def __init__(self,id, name, url, description, title, author, urlToImage, content,publishedAt ):
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.title = title
        self.author = author
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt


class Source:
    '''
    Source class to define Source object
    '''
    def __init__(self,id, name, language):
        self.id = id
        self.name = name
        self.language = language
        