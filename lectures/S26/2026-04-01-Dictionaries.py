# Quiz 7 -- For Loops (Friday)
# Homework 8 -- Dictionaries (Monday)
#
# Begin thinking about your final project

enroll_dict = {'CSCI15001': 26, 'CSCI150L1': 15, 'CSCI150L2': 11, 'CSCI15101': 12, 'CSCI151L1': 12, 'CSCI27001': 22}

# We use a for loop to walk across a dictionary:

def explode_dictionary(d: dict[str, int]):
    for k in d:
        print(k, d[k])


# Given the dictionary above, find the total number of students enrolled
def enrolled(d: dict[str, int]) -> int:
    1


# Modify the above so it does not include students enrolled in labs

def enrolled_lecture(d: dict[str, int]) -> int:
    1


# Given a list of strings (words), build a dictionary which:
# * is keyed on the length of the words
# * the value is the count of the number of such words

# For example:
# lst = ['the', 'main', 'point', 'about', 'dictionaries', 'is', 'that', 'they', 'are', 'fun']
#
 # should return
 # {3: 3, 4: 3, 5: 2, 12: 1, 2: 1}

def length_dict(lst: list[str]) -> dict[int, int]:
    out_dict = {}
    for word in lst:
        if len(word) not in out_dict:
            out_dict[len(word)] = 0
        out_dict[len(word)] += 1
    return out_dict



def word_count(filename: str) -> dict[int, int]:
    out_dict = {}
    f = open(filename, 'r')
    for line in f.readlines():
        word = line.strip()
        if len(word) not in out_dict:
            out_dict[len(word)] = 0
        out_dict[len(word)] += 1
    return out_dict


def sorted_explode(d):
    for k in sorted(d):
        print(k, d[k])