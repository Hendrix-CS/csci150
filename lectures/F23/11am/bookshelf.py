from book import *

class Bookshelf:

    def __init__(self):
        self.books: list[Book] = []

    def add(self, book: Book):
        self.books.append(book)

    # We could add functions to e.g.
    #   - look up a book by title or author
    #   - take a book off the shelf
    #   - calculate some statistics about the books

# Read in an entire bookshelf from a file
def parse_bookshelf(bookshelf_file_name: str) -> Bookshelf:
    shelf = Bookshelf()
    file = open(bookshelf_file_name, 'r')
    for line in file.readlines():
        shelf.add(parse_book(line.strip()))

    file.close()
    return shelf