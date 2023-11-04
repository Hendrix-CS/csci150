from book import *

class Bookshelf:

    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def save(self, bookshelf_file_name: str):
        file = open(bookshelf_file_name, 'w')
        for book in self.books:
            file.write(book.format() + '\n')
        file.close()

def parse_bookshelf(bookshelf_file_name: str) -> Bookshelf:
    bookshelf = Bookshelf()

    file = open(bookshelf_file_name, 'r')
    for book_data in file.readlines():
        bookshelf.add_book(parse_book(book_data))

    file.close()
    return bookshelf
