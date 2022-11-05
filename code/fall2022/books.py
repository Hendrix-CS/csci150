# Example: books + bookshelves

from typing import *


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

        self.pages_read = 0
        self.read_count = 0
        self.rating = 0

    def read(self, pages: int):
        self.pages_read += pages
        if self.pages_read >= self.pages:
            self.pages_read = self.pages
            self.read_count += 1

    def mark_read(self):
        self.read_count += 1

    def rate(self, rating: int):
        self.rating = rating

    def reread(self):
        self.pages_read = 0

    def is_read(self):
        return self.read_count > 0

        # if self.read_count > 0:
        #     return True
        # else:
        #     return False

    def __lt__(self, other: 'Book'):
        return self.author < other.author

    def __repr__(self):
        return f'{self.title} by {self.author}'

class Bookshelf:
    def __init__(self, book_limit: int):
        self.book_limit = book_limit
        self.books: List[Book] = []

    def add_book(self, book: Book):
        if len(self.books) < self.book_limit:
            self.books.append(book)
        else:
            print("Book doesn't fit!")

    # Sort by author
    def organize(self):
        self.books.sort()

    def find_unread(self):
        for book in self.books:
            if not book.is_read():
                return book
        return None

    def __repr__(self):
        book_strs = []
        for book in self.books:
            book_strs.append(str(book))

        return '\n'.join(book_strs)

def main():
    shelf = Bookshelf(2)

    mce = Book('A Memory Called Empire', 'Martine, Arkady', 800)
    mce.read(300)
    mce.read(500)
    shelf.add_book(Book('Leaves of Grass', 'Whitman, Walt', 456))
    shelf.add_book(mce)

    shelf.organize()
    print(shelf)

    print(shelf.find_unread())

main()
