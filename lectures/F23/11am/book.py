from counter import *

class Book:

    # Information to keep track of:
    # - title: str
    # - num_pages: int
    # - author: str
    # - chapters: int
    # - finished: bool
    # - bookmark: Counter
    # - dogears: list[int]

    def __init__(self, title: str, num_pages: int, author: str, chapters: int):
        self.title = title
        self.num_pages = num_pages
        self.author = author
        self.chapters = chapters
        self.finished = False
        self.bookmark = Counter(num_pages)
        self.dogears = []

    def finish(self):
        self.finished = True

    def is_finished(self) -> bool:
        return self.finished

    def read(self, pages: int):
        self.bookmark.add(pages)
        if self.bookmark.get_count() == self.num_pages:
            self.finished = True

    # Dogear the current page
    def dogear(self):
        self.dogears.append(self.bookmark.get_count())

    def format(self) -> str:
        return f'{self.title};{self.num_pages};{self.author};{self.chapters};{self.finished};{self.bookmark.get_count()};{self.dogears}'

# Read in a line of data about a book and turn it into a Book object
#
# e.g.
#   "The Odyssey;500;Homer;24;False;120;[35,29]"
def parse_book(book_data: str) -> Book:
    fields: list[str] = book_data.split(';')
    book: Book = Book(fields[0], int(fields[1]), fields[2], int(fields[3]))
    if fields[4] == 'True':
        book.finish()

    book.bookmark.add(int(fields[5]))
    dogear_strs = fields[6][1:-1].split(',')
    for page in dogear_strs:
        if page != '':
            book.dogears.append(int(page))

    return book
