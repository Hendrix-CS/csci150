from counter import *

class Book:

    # What variables/fields do we want to store?
    # - num_pages: int
    # - current_page: Counter
    # - title: str
    # - author: str
    # - genre: str

    def __init__(self, num_pages: int, title: str, author: str, genre: str):
        self.num_pages = num_pages
        self.title = title
        self.author = author
        self.genre = genre
        self.currently_reading: bool = False
        self.current_page: Counter = Counter(num_pages)

    def start_reading(self):
        self.currently_reading = True
        self.current_page.reset()

    def stop_reading(self):
        self.currently_reading = False

    def resume_reading(self):
        self.currently_reading = True

    def read(self, num_pages: int):
        self.currently_reading = True
        self.current_page.add(num_pages)

    def format(self) -> str:
        return f'{self.num_pages},{self.title},{self.author},{self.genre},{self.currently_reading},{self.current_page.get_count()}'

# Given a line of data describing a book, construct a Book object
# num_pages,title,author,genre,currently_reading,current_page
# e.g.
#   "300,The Odyssey,Homer,Epic,True,192"
def parse_book(book_data: str) -> Book:
    fields: list[str] = book_data.split(',')
    the_book = Book(int(fields[0]), fields[1], fields[2], fields[3])
    if fields[4] == 'True':
        the_book.start_reading()
    the_book.current_page.add(int(fields[5]))

    return the_book
