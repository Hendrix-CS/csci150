##
# We want to build a pair of related classes:
#  Book -- which will represent a book, with the following attributes:
# * Title
# * Number of Pages
# * Current Page
# * Whether you have previously read the book

##
# Methods:

# Shelf Class -- will be a list of books, mimicking a single shelf:
# * Width -- how many books it can contain
# * books -- which books (if any) are on the shelf

# Methods:

# Add book to a shelf -- be careful if shelf is full!
# Remove book from shelf
# List the books on the shelf



class Book:

    def __init__(self,title: str, pages: int ):
        self.title = title
        self.pages = pages

        self.curr_page = 0
        self.completed = False

        # Just being fancy
        self.pretty_title = f'\x1B[3m{self.title}\x1B[0m'




    # The following method is useful, but *NOT* necessary in CSCI 150.
    # Essentially, it makes the printing of the book objects look nice
    def __str__(self):
        return self.pretty_title

    def read(self,p):
        self.curr_page += p

        if self.curr_page > self.pages:
            self.completed = True

            self.curr_page = 0

class Shelf:

    def __init__(self,cap: int):
        self.capacity = cap
        self.books = []

    ## Add Book
    def add_book(self,b):
        if len(self.books) < self.capacity:
            self.books.append(b)
        else:
            print('The shelf is full.')


    ## Remove Book
    def remove_book(self,b):
        if b in self.books:
            self.books.remove(b)
        else:
            print(f'{b} is not on the shelf')

    def list_books(self):
        for book in self.books:
            print(book)
