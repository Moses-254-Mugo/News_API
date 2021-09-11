class Article:
    '''
    Article class to define Article object
    '''
    def __init__(self,source, url_img, description, title, author):
        self.source = source
        self.url_img = url_img
        self.description = description
        self.title = title
        self.author = author


class Source:
    '''
    Source class to define Source object
    '''
    def __init__(self,id, name, description, url_img):
        self.id = id
        self.name = name
        self.description = description
        self.url_img = url_img
