 #Create a single inheritance program for a Library system.
 #Create a parent class named Book with:
 #title
 #author
 #display_book_details() method

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("the title of the book is :", self.title)
        print("the Author of the book is:", self.author)


# Child Class (Single Inheritance)
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        # Call parent constructor
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        # Call parent method
        self.display_book_details()
        print("the name of the person issued to is :", self.issued_to)
        print("the date of issued date is:", self.issued_date)


# Creating object of IssuedBook
book1 = IssuedBook("Python", "Rossum", "sona", "04-02-2026")

# Display all details
book1.display_issued_book_details()