# Doublets!
import dictionary

def get_word(word_name):
    valid = False
    while not valid:
        word = raw_input("What is the " + word_name + " word? ")
        if dictionary.valid_word(word, "english2.txt"):
            valid = True
        else:
            print "That is not a word. Try again."
    return word

def get_starting_word():
    return get_word("starting")

def get_ending_word(start):
    valid = False
    while not valid:
        target = get_word("ending")
        if len(target) == len(start):
            valid = True
        else:
            print target + " is not the same length as " + start + ".  Try again."

    return target

def int_input(prompt):
    valid = False
    while not valid:
        s = raw_input(prompt)
        if s.isdigit():
            valid = True
        else:
            print "That is not a number. Try again."
    return int(s)

def get_position(current):
    valid = False
    while not valid:
        p = int_input("Enter a position. ")
        if 1 <= p and p <= len(current):
            valid = True
        else:
            print "Invalid position."

    return p

def play_doublets(start, target):
    current = start
    path = [start]

    won = False
    while not won:
        print "Current: " + current
        print "Target:  " + target
        pos = get_position(current)

def main():
    start  = get_starting_word()
    target = get_ending_word(start)
    play_doublets(start, target)

# main()
