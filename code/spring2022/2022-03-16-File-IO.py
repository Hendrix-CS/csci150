from typing import *

# Project #2 -- Not officially assigned until after Break
# You will write a word game
# I showed an example of wordle -- but am not giving you all of the code
#
#
# Here is my main:
#
#
#
# def main():
#     print_instructions()
#     cont = True
#     while cont:
#         level = set_level()
#         play_game(level)
#         cont = play_again()
#     print('Thank you for playing wordleish!')

# First, Tuples

# Preview tuples before lab today

# New data type -- a *tuple*

# A tuple is an ordered collection of objects -- which sounds like a list
# But, a tuple is *immutable*

# Tuple Examples

# tup = (3, 6, 8, 11)
# print(tup[1])

# Run in console
# tup[3] = 17

# note that if lst = [3, 6, 8, 11]
# then lst[3] = 17 *does* work!

# Like lists, the entries in a tuple can be anything -- typically, each entry is the same
# type of object (they are all ints, all strings, all Lists of String)
# *but* since they are immutable, we are more likely to mix things in.

# One use of a tuple is when a function should return more than one value:

## Given a list of ints, return *two* lists, one with the even values, and one with the odds
#
# def even_odd_list(lst: List[int]) -> Tuple[List[int],List[int]]:
#     evens = []
#     odds = []
#     for entry in lst:
#         if entry % 2 == 0:
#             evens.append(entry)
#         else:
#             odds.append(entry)
#
#     return evens, odds
#
# def main():
#     lst = [5, 6, 7, 8, 10]
#     my_tup = even_odd_list(lst)



# Being able to read in input from a file
# and/or save output to a file is often quite useful
#
# The Todo List Manager lab had you do this, but with pre-written code
# Today, we'll learn how to do this on your own.

# Being able to read in and write to a file may be quite useful on Project #2 (official assigned right after break)

# This bit of python code takes you through how to do that:

##################
# To read from a file:

# Give the input file a variable name in python:

#file_in = open(<file_name>,'r')    # the 'r' means to read the file
# This opens the file and allows you to read through it
# If the file is small, try
#
#a = file_in.read()  # a will now be a string with all special characters

# Or read line by line:
# for line in file_in.readlines():
#   b = line.strip()  # the strip will remove any newline characters

# file_in.close()  # will close the file after you are done

# Example:

# my_first_file =open('sample-text-file.txt','r')
#
# a = my_first_file.read()
#
# my_first_file.close()
#
# print(len(a))
#
# print(a)
# print(a.count('s'))



# This works well when you want to read in  file (typically fairly small)
# and digest it at once.

# Sometimes, though, you want to run through the file line-by-line
#   -- either the file is large and you want to not soak up a bunch of memory
#   -- or the lines themselves have special meaning.

# my_next_file = open('sample-text-file.txt','r')
# for line in my_next_file.readlines():
#     b = line.strip()
#     print(len(b))

# my_next_file.close()

# Take, for example, the list of English words, from the 'Mutation' Lab, english3.txt

# We could of course do:
#
# word_file =open('english3.txt','r')
#
# words = word_file.read()
#
# word_file.close()
# # #
# print(len(words))
# #
# # print(words)
# # print(words.count('s'))
# # print(words.count('\n'))
#
# # You can re line-by-line by using the following code
#

# word_file2 = open('english3.txt','r')
#
# word_list = [] # this will be a list, which will hold each word in the dictionary as an item
# for line in word_file2.readlines():     # this reads through one line at a time.
#     word =  line.strip()   # 'line' is the word, but has the \n included
#                            # .strip() will remove any leading and trailing spaces and end of line characters
#     word_list.append(word)
#
#
# word_file2.close()  # this is not strictly required, but is good practice to close your file
# #
# print(len(word_list))
#
# #print(word_list)
# #
# print('space' in word_list)
# print('abcd' in word_list)




# ##################
# # Writing to a file
#
# # This follows a similar path:
# #file_out = open(<file_name>,'w') # the 'w' means write -- and will erase anything saved in that file previously
#
# #file_out.write(string) will write the string to the file
# # file_out.close()  # closes the file
#
# out_file = open('test1.txt','w')
#
# out_file.write('Hi\n')
# out_file.write('Bye')
#
# out_file.close()

# Example -- Prompt the user to enter strings
# continue to prompt until they type 'Exit.'
# Then ask them for a file name
# Write out their strings (except 'Exit') one line at a time to that file:
#
# def make_file():
#     cont = True
#     lst = []
#     while cont:
#         word = input('Please enter a string (type \'Exit\' to stop: ')
#         if word == 'Exit':
#             cont = False
#         else:
#             lst.append(word)
#
#     file_name = input('Please enter a file name to save to: ')
#     out_file1 = open(file_name,'w')
#
#     for item in lst:
#         out_file1.write(item + '\n')
#
#     out_file1.close()


#make_file()
###############
# IMPORTANT!! #
###############

# When you open a file to write, Python does not check to see if that file name is currently
# in use. It simply overwrites whatever is there!



# f = open('My Senior Capstone.docx','w')
# f.close()

# f = open('temp.txt','w')
# f.write('fgf')
# f.close()


##########################
# Putting it together
#########################

# Look at the file course_list.txt which contains names, classifications (freshman, sophomore, etc) and GPA
# It is delimited by the semicolon, ;

# Lets read it in, and create 4 lists, one for each classification, where the entries are themselves tuples of name and gpa


def class_list() -> Tuple[List[Tuple[str,float]],List[Tuple[str,float]],List[Tuple[str,float]],List[Tuple[str,float]]]:
    fresh_list = []
    soph_list = []
    junior_list = []
    senior_list = []

    data_file = open('course-list.txt','r')

    for line in data_file.readlines():
        data = line.strip().split(';')


        if data[1] == 'Freshman':
            fresh_list.append((data[0],float(data[2])))
        elif data[1] == 'Sophomore':
            soph_list.append((data[0],float(data[2])))
        elif data[1] == 'Junior':
            junior_list.append((data[0],float(data[2])))
        elif data[1] == 'Senior':
            senior_list.append((data[0],float(data[2])))

    data_file.close()

    return fresh_list, soph_list, junior_list, senior_list

