from management import Management

running = True

greet = """
Welcom to our Laibrary Management system
Choose the numbers to began
1. add books
2. remove a book if exist
3. issue a book
4. return a book
5. show all books
6. Exit
Enter your options: """

# laibrary = Management()
# laibrary.issue_book('test1','2024-01-20')
# print(laibrary.books)
# laibrary.show_books()

while running:
    user_choice = input(greet)
    try:
        user_choice = int(user_choice)
        laibrary = Management()

        if user_choice == 1:
            book_name = input("Enter your book name: ").lower()
            book_date = input("Enter your book date: ").lower()
            book_author = input("Enter your book author: ").lower()
            book_add= laibrary.add_books(book_name,book_author,book_date)
            print(book_add['message'])
        elif user_choice == 2:
            book_name = input("Enter your book name: ").lower()
            book_date = input("Enter your book date: ").lower()
            book_remove = laibrary.remove_book(book_name,book_date)
            print(book_remove['message'])  
        elif user_choice == 3:
            book_name = input("Enter your book name: ").lower()
            book_date = input("Enter your book date: ").lower()
            book_issue = laibrary.issue_book(book_name,book_date)
            print(book_issue['message'])
        elif user_choice == 4:
            book_name = input("Enter your book name: ").lower()
            book_date = input("Enter your book date: ").lower()
            book_return = laibrary.return_book(book_name,book_date)
            print(book_return['message'])
        elif user_choice == 5:
            laibrary.show_books()
            
        elif user_choice == 6:
            running = False
        else:
            print("Sorry Wrong entry")
    except Exception as e:
        print('Please enter valid input', str(e))
    
    

print("Thanks for using Please restart to start.")
    
