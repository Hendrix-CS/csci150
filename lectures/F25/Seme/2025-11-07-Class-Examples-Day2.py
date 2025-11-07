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






@dataclass
class Shelf:
    size: int
    books: list['book']

#### Some notes:
# We don't currently have a way to keep a book from being shelved on more than one shelf
# That would take additional work, but could be accomplished
#
# We could also build a BookCase class, which would combine together multiple shelves





