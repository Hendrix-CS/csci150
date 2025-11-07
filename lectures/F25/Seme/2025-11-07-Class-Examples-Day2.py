from dataclasses import dataclass
import random

# Reminders
# Class Homework is due on Monday
# Final Project Design Document is due on Friday of next week




# Books and Shelves Example

# First, we'll make a Book class
# We have a text file of books and want to make a Book object for each
@dataclass
class Book:
    title: str
    pages: int
    curr_page: int = 0
    read: bool = False

    def read_book(self,read_pages: int):
        self.curr_page += read_pages

        if self.curr_page >= self.pages:
            self.read = True
            self.curr_page = 0

            print(f'You have finished {self.title}.')




def book_list_creator(file_name: str):
    lst = []

    with open(file_name,'r') as f:
        for line in f:
            data = line.strip().split(';')
            title = data[0]
            pages = int(data[1])

            lst.append(Book(title,pages))

        f.close()




    return lst











@dataclass
class Shelf:
    size: int
    books: list['book']

    def shelve_book(self, b):
        if len(self.books) < self.size:
            self.books.append(b)
        else:
            print('The shelf is full.')

    def remove_book(self,b):
        if b in self.books:
            self.books.remove(b)
        else:
            print(f'{b.title} is not on the shelf.')

#### Some notes:
# We don't currently have a way to keep a book from being shelved on more than one shelf
# That would take additional work, but could be accomplished
#
# We could also build a BookCase class, which would combine together multiple shelves





