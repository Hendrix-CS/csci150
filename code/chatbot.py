############
# Creating an Eliza Chatterbot
# 11/24/2014
# Mark Goadrich
############

import random

class Chatter():

    def __init__(self, name):
        self.name = name

    def intro(self):
        return self.name.upper() + ": " + "Hello, I am " + \
               self.name.upper() + ". How can I help you? "

    def response(self, text):
        pass

class Eliza(Chatter):

    def __init__(self):
        Chatter.__init__(self, "ELIZA")

    def response(self, text):
        return self.name.upper() + ": " + "What makes you say that?"

class User(Chatter):

    def response(self, text):
        return input(self.name.upper() + ": ")

def main():

    n = input("What is your name? ")
    e = Eliza()
    m = User(n)
    er = e.intro()
    print(er)
    finished = False
    while not finished:
        r = m.response(er)
        if r.upper() == "DONE":
            finished = True
        else:
            er = e.response(r)
            print(er)
    print("Goodbye!")

main()
