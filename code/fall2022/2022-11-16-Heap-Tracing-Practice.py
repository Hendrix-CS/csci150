from typing import *

# Reminders:
#
# Class/Dictionary Homework due today -- will be returned on Teams,
#     with instructions if not Complete
# Project #2 redos are due on Friday
# Final Project Design Document due Friday as well (Teams)
# Exam #3
# -- in class Monday, November 21
# -- take home passed out Friday, due by Tuesday evening, 11:59pm

#
#
##############################
# Today: Heap Tracing Practice
#
# Sample Solutions can be found:
# https://hendrix-my.sharepoint.com/:b:/g/personal/seme_hendrix_edu/EW8ofF_FWupFh-QhHbbJw0cB94boXhdfG3LUK7a-RH-AMA?e=YC9DhM

#1
def f1(y: int) -> int:
    if y % 2 == 0:
        return y // 2
    else:
        return y + 5

def main1():
    a_list = [7, 2, 1, 4]
    b_list = a_list

    for i in range(len(a_list)):
        a_list[i] = f1(a_list[i])

    print(a_list)
    print(b_list)

main1()


#2
def main2():
    a_dict = {1: 'hi', 2: 'there', 3: 'how', 4: 'are', 5: 'you?'}
    b_dict = {}

    for key in a_dict:
        b_dict[key] = len(a_dict[key])

    a_dict[6] = 'Fine!'

    print(a_dict)
    print(b_dict)

main2()


#3
def g1(lst: List[int], s: str, n: int) -> int:
    if n < len(lst):
        lst[n] = len(s)
        return n
    else:
        return len(s)

def main3():
    x_list = [5, 2, 1, 9]
    y_list = x_list

    a_dict = {'see': 2, 'you': 5, 'later': 1}
    b_dict = a_dict
    for key in b_dict:
        b_dict[key] = g1(y_list, key, b_dict[key])

    print(x_list)
    print(y_list)

    print(a_dict)
    print(b_dict)

main3()

