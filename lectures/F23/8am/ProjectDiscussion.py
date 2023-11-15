# Three main issues on Project 2.

# 1: functions that were mostly duplicates.

# def play_easy():
#     # do stuff
#     if len(guess) != 5:
#         ...
#
# def play_medium():
#     # do stuff
#     if len(guess) != 7:
#         ...
#
# def play_hard():
#     # do stuff
#     if len(guess) != 9:
#         ...
#
# # Better:
#
# def guess_len(difficulty: int):
#     if difficulty == 1:
#         return 5
#     elif ...
#
# def play(difficulty: int):
#     # do stuff
#     if len(guess) != guess_len(difficulty):

# If you have multiple pieces of code that are *almost* but not quite the same,
# make them into a single function that takes one or more parameters
# to fill in for the parts that are not the same.

# 2.

# Suppose we have a program that should do three tasks:
# task 1, then task 2, then task 3.

# Not a good way to organize the code:
# Each function should not be responsible for what happens after it.

# def task3():
#     # do task 3 stuff
#     # ask user if they want to play again
#     if yes:
#         main()
#
# def task2():
#     # do task 2 stuff
#     task3()
#
# def task1():
#     # do some stuff
#     task2()
#
# def main():
#     task1()
#
#
# # Better:
#
# def task2():
#     # do task 2 stuff
#
# def task1():
#     # do task 1 stuff
#
# def main():
#     play_again = True
#     while play_again:
#       task1()
#       task2()
#       task3()
#       play_again = ask_user()

def main():
    print("Game!")
    play_again = input("Do you want to play again? ")
    if play_again == 'Y':
        main()

    print("OK, goodbye!")


main()