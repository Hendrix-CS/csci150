############
# Creating an Eliza Chatterbot
# 11/28/2015
# Mark Goadrich
############

import random

class Chatter:

    def __init__(self, name):
        self.name = name

    def intro(self):
        return self.name.upper() + ": " + "Hello, I am " + \
               self.name.upper() + ". How can I help you? "

    def outro(self):
        return self.name.upper() + ": Goodbye!"

    def get_response(self, text):
        pass

    def response(self, text):
        return self.name.upper() + ": " + self.get_response(text)

class Eliza(Chatter):

    def __init__(self):
        Chatter.__init__(self, "ELIZA")

    ### BEGIN CHANGES HERE ###
        
    def get_response(self, text):
        return "What makes you say that?"

    ### END CHANGES HERE ###

class User(Chatter):

    def response(self, text):
        return raw_input(self.name.upper() + ": ")

def main():

    n = raw_input("What is your name? ")
    e = Eliza()
    m = User(n)
    er = e.intro()
    print er
    finished = False
    while not finished:
        r = m.response(er)
        if r.upper() == "GOODBYE":
            finished = True
        else:
            er = e.response(r)
            print er
    print e.outro() 

main()
