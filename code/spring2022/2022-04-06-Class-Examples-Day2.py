from typing import *

# Reminders
# Project #2 is due on Monday
# Last Homework set (coding with dictionaries and classes)
#    is due next Wednesday
# Practice Exam #3 is posted, along with sample solutions
# We will use it for review next Friday, but you are welcome to start on it
#    and ask me any questions individually as well
# Exam #3 is Monday, April 18 with the Take Home due on Wednesday, April 20th


####################################################
# Books and Shelves Example

class Book:

    def __init__(self,title: str, pages: int):
        self.title = title
        self.pages = pages
        self.curr_page = 0
        self.completed = False
        self.pretty_title = f'\x1B[3m{self.title}\x1B[0m'

    def __repr__(self):
        return f'Book("{self.title}", {self.pages})'

    def __str__(self):
        temp = ''
        if self.completed:
            temp = ' You have read this book before.'

        return f'The book {self.pretty_title} contains {self.pages} pages. You are on page {self.curr_page}.{temp}'

    def read(self, n: int):
        self.curr_page +=n
        if self.curr_page >= self.pages:
            self.curr_page = 0
            self.completed = True
            print('You have finished the book!')

    def finished(self):
        return self.completed




class Shelf:

    def __init__(self, width: int):
        self.width = width
        self.books = []

    def __repr__(self):
        return f'Shelf({self.width})'

    def __str__(self):
        return f'This shelf contains the following books: {", ".join([a.pretty_title for a in self.books])}'

    def is_full(self):
        return len(self.books) == self.width

    def book_on_shelf(self, book) -> bool:
        return book in self.books

    def shelve_book(self, book: Book):
        if not self.is_full():
            self.books.append(book)
        else:
            print('The shelf is full.')

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f'{book.pretty_title} is not on the shelf.')

    def unread_books(self):
        temp = []
        for book in self.books:
            if not book.finished():
                temp.append(book.pretty_title)

        if len(temp) == 0:
            print('There are no unread books on the shelf.')
        else:
            print(f'The unread books on this shelf are {", ".join(temp)}')





def book_builder():
    book_list = []
    f = open('books.txt','r')

    for item in f.readlines():
        info = item.strip().split(',')
        title = info[0]
        pages = int(info[1])

        book = Book(title, pages)
        book_list.append(book)

    f.close()

    return book_list


def book_finder(title: str, book_list: List[Book]) -> Book:
    for book in book_list:
        if title == book.title:
            return book
    print('That book is not available.')
    return None






#### Some notes:
# We don't currently have a way to keep a book from being shelved on more than one shelf
# That would take additional work, but could be accomplished
#
# We could also build a BookCase class, which would combine together multiple shelves





