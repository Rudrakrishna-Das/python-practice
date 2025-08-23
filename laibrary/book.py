import uuid
class Book:
    """
    This class belongs to book.
    Here we can create a book,
    methods:
    1. Convert Book instance to dictionary
    2. A class method which convert a dictionary to instance
    """
    def __init__(self,name,author,date,is_active=True,is_issue=False,id=None):
        self.id = id if id is not None else str(uuid.uuid4())
        self.name = name
        self.author = author
        self.date = date
        self.is_issue = is_issue
        self.is_active = is_active
    
    def to_dict(self):
        book_data ={
            'id':self.id,
            'name':self.name,
            'author':self.author,
            'date':self.date,
            'is_issue':self.is_issue,
            'is_active':self.is_active
        }
        return book_data
    
    @classmethod
    def from_dict(cls,dict):
        cls.id = dict['id']
        cls.name = dict['name']
        cls.author = dict['author']
        cls.date = dict['date']
        cls.is_issue = dict['is_issue']
        cls.is_active = dict['is_active']