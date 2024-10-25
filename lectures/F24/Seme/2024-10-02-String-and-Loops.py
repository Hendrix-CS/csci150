# Project #1 -- Due Friday
# Homework -- Function Stack Tracing -- Due Monday
# Comments on CodingBat & outside help



# Quick reminder about strings

s = 'My string'
t = 'abcdefg'

# s = s.upper()
# #print(s.upper())
# print(s)
#
# # lower
#print(s.lower())
#
# print(s) #notice that s.lower() and s.upper() don't actually change s
#
#print('fbXtR%& *'.lower())

# count
#
# print(s.count('x'))
# print(s.count('n'))
# #
# print('abcABCabcdeab'.count('abc'))

#print('abcABCabcdeab'.count('a'))

# find

#print(s.find('t'))
#
#print('abcdabcdabcde'.find('z'))

# replace

# print(s.replace('y','TTT'))
# #
# print('abcdabcdabcd'.replace('b',"X"))


#print('12303'.isdigit())

#print('-12303'.isdigit())

## Looping with strings


def string_counter(s: str, char: str) -> int:
    count = 0
    i = 0
    while i < len(s):
        if s[i] == char:
            count += 1
        i += 1
    return count

## Typical loop structure:

# accum = starting value
# i = 0
# while i < len(s):
#     do things to s/accum as appropriate
#
#     i += 1
#
# return accum


def string_replace(s: str, old: str, new: str) -> str:
    new_str = ''
    i = 0

    while i < len(s):
        if s[i] == old:
            new_str += new
        else:
            new_str += s[i]

    return new_str


def reverse(s: str) -> str:
    new_str = ''
    i= 0
    while i < len(s):
        new_str = s[i] + new_str
        i += 1

    return new_str

def reverse2(s: str) -> str:
    new_str = ''
    i= len(s) - 1
    while i >= 0:
        new_str = new_str + s[i]
        i -= 1

    return new_str

# Write is_inorder(s: str) -- will take in a lower case word
# and return True if the characters all appear in alphabetical order
# repeated letters are ok:
# 'hiss' is True, as is 'art', but 'sleet' is False



def is_inorder(s: str) -> bool:
    i = 0
    while i < len(s) - 1:
        # check two character -- return False if not in order
        if s[i] > s[i+1]:
            return False
        i += 1

    return True

















def int_input(prompt: str) -> int:
    is_okay = False
    while not is_okay:
        answer = input(prompt)
        if answer.isdigit():
            is_okay = True
        elif len(answer) > 0 and answer[0] == '-' and answer[1:].isdigit():
            is_okay = True
        else:
            print('That is not a valid integer. Please try again.')

    return int(answer)