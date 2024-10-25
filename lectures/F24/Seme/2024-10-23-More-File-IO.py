from typing import *

# Project #2 due one week from today
# Homework 9 - File IO due on Monday
#   -- both are turned in on Teams

# Example -- Prompt the user to enter strings
# continue to prompt until they type 'Exit.'
# Then ask them for a file name
# Write out their strings (except 'Exit') one line at a time to that file:
# #
def make_file():
    f_out = open('output_file.txt','w')
    cont = True

    while cont:
        word = input("Enter a word. Use 'Exit' to stop.")
        if word == 'Exit':
            cont = False
        else:
            f_out.write(word + '\n')

    f_out.close()

def read_data():
    f_in = open('data-practice.txt','r')
    header = True
    sum = 0
    count = 0
    for line in f_in.readlines():
        data = line.strip()
        data = data.split(',')
        if not header:
            count += 1
            sum += float(data[2][1:])

        header = False

    f_in.close()
    return sum / count

# Read Data File
# The file 'data-practice.txt' is a comma-delimited
# file. It is (made-up) data representing customer data:
# order number, customer ID, purchase price, state

# Write a function which reads in the file and
#  returns the average purchase for an order