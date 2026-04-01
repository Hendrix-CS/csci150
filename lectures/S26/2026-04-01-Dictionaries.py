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
    c = 0
    for k in d:
        c += d[k]


    return c


# Modify the above so it does not include students enrolled in labs

def enrolled_lecture(d: dict[str, int]) -> int:
    c = 0
    for k in d:
        if k[7] != 'L':
            c += d[k]

    return c


# Given a list of strings (words), build a dictionary which:
# * is keyed on the length of the words
# * the value is the count of the number of such words

# For example:
lst = ['the', 'main', 'point', 'about', 'dictionaries', 'is', 'that', 'they', 'are', 'fun']
#
 # should return
 # {3: 3, 4: 3, 5: 2, 12: 1, 2: 1}

def length_dict(lst: list[str]) -> dict[int, int]:
    out_dict = {}
    for word in lst:
        length = len(word)

        # if the length is not already in the dictionary
        if length not in out_dict:
            out_dict[length] = 1
        else:
            out_dict[length] += 1

        # # or:
        # if length not in out_dict:
        #     out_dict[length] = 0
        # out_dict[length] += 1



    return out_dict

# WHen you build a dictionary from data, you have to first check if the current key
# is *not* in the dictionary -- if not, you need to add it


# Making the letter frequency count dictionary from the 'Alice.txt'' file
def freq_count(filename: str) -> dict[str, int]:
    out_dict = {}
    f = open(filename,'r')
    for char in f.read():
        if char.isalpha():
            k = char.lower()
            if k not in out_dict:
                out_dict[k] = 0
            out_dict[k] += 1

    f.close()

    total = 0
    for k in out_dict:
        total += out_dict[k]

    new_dict = {}
    for k in out_dict:
        new_dict[k] = out_dict[k] / total






    return new_dict



# Then, we will turn these into their decimal frequencies



# Can we sort?
def sorted_explode(d):
    for k in sorted(d):
        print(k, d[k])