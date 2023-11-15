# Common issues on project 2

# 1. Multiple functions that are almost, but not quite, the same.

# def play_easy():
#   ... do some stuff ...
#   if len(guess) != 5:
#      ....
#
# def play_medium():
#   ... do some stuff ...
#   if len(guess) != 7:
#      ....
#
# def game():
#    if difficulty == 'easy':
#       play_easy()
#    elif difficulty == 'medium':
#       play_medium()
#    ...
#
# Instead, make one function which takes one or more parameters representing the part that is different.
#
# e.g.
#
# def play(guess_len):    # or just give it the difficulty as a parameter.
#    ... do some stuff ...
#    if len(guess) != guess_len:
#       ....
#
# def game():
#    if difficulty == 'easy':
#       play(5)
#    elif difficulty == 'medium':
#       play(7)
#    ...
#
# 2. Functions calling each other in a chain instead of in a hierarchy.
#
# def task3():
#    ....
#
# def task2():
#    ... do task 2 stuff ...
#    task3()
#
# def task1():
#   ... do task 1 stuff ...
#   task2()
#
# def main():
#    task1()

# A function should not be responsible for "what happens next".
#
# Better:

# def main():
#   task1()
#   task2()
#   task3()

# 3. Functions calling themselves in order to repeat.

def main():
    print("Play the game!")
    again = input("Do you want to play again? ")
    if again == 'Y':
        main()

    print("Goodbye")

main()

# Instead, use a loop!