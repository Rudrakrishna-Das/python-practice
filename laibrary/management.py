from storage import Storage
from book import Book
class Management:
    """
    Here our Mange ment will go on
    Inititally we load all books if that exists in a json file and store in book variable
    or we just store a empty array in the book variable
    Methods
    All Laibrary related functions stored here

    """
    def __init__(self):
        self.books = []
        self.load_books()
    
    def load_books(self):
        book_data = Storage.read_from_file()
        if book_data['success']:            
            for book_details in book_data['result']:
                my_new_book = Book(**book_details)            
                self.books.append(my_new_book)
        else:
            self.books = []

    def add_books(self,name,author,date):
        book_details = self.find_book(name,date)
        if book_details['success']:
            book_details['book'].is_active = True
            self.books[book_details['index']] = book_details['book']
            return self.save_books()

        my_book = Book(name,author,date)
        self.books.append(my_book)
        return self.save_books()


        
    def save_books(self):
        print(self.books)
        all_books = [book.to_dict() for book in self.books]
        return Storage.write_to_file(all_books)
    
    def issue_book(self,name,date):
        book_details = self.find_book(name,date)
        print(book_details)

        if book_details['success'] is False:
            return book_details
        else:
            if book_details['book'].is_issue:
                    return{'success':False,'message':'Book Alredy issued'}
            book_details['book'].is_issue = True
            self.books[book_details['index']] = book_details['book']
            
            return self.save_books()
        
    def return_book(self,name,date):
        book_details = self.find_book(name,date)
        if book_details is False:
            return book_details
        else:
            if book_details['book'].is_issue:
                book_details['book'].is_issue = False
                self.books[book_details['index']] = book_details['book']
                
                return self.save_books()
            return{'success':False,'message':'Book Alredy in the Storage'}
        
    def remove_book(self,name,date):
        book_details = self.find_book(name,date)
        if book_details is False:
            return book_details
        else:
            if book_details['book'].is_active:
                book_details['book'].is_active = False
                self.books[book_details['index']] = book_details['book']
                self.save_books()
                return {'success':True, 'message':'Book Removed'}
            return{'success':False,'message':'Book Alredy in the Storage'}
            
    def find_book(self,name,date):
        if len(self.books) == 0:
             return {'success':False,'message':"Please Add a book first!"}
        

        for index,book in enumerate(self.books): 
            print(book.name,name)           
            if book.name == name and book.date == date:
                return {'success':True,"index":index, "book":book}
            
        return {'success':False,'message':"Please check the info"}
            
    def show_books(self):
        for book in self.books:
            print(f"{book.name.title()} written by {book.author.title()} on {book.date}")

