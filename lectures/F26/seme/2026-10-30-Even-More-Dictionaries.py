# NOTE -- I completely forgot to start the meeting on Teams and record today.
# If you have questions, I am happy to talk with you -- and *SORRY*
# I think Dr. Yorgey did record his, so you can watch that as well.


# Reminders
# Quiz Today -- For Loops
# Final Project
#   -- start to think about what you might do: I am happy to help you brainstorm
#   -- design document due Monday, November 16
#   -- Project Due (& Demo Day) Friday, December 11 (9am)

# Dictionaries, part iii

# when building a dictionary, you often encounter a new potential key:
# -- if that key is not already in the dictionary add it (and its value)
# -- if it is in the dictionary, update its value as needed

# We saw this last time with the str_freq function

# Given a string of words, all separated by a single empty space
# return a dictionary whose keys are integers and values are a *list* of the
# words with that length.

s = 'The best thing about dictionaries is that they are a lot of fun'
print(s.split(' '))

def length_word(s: str) -> dict[int, list[str]]:
    out_dict = {}
    s_lst = s.split(' ')
    for word in s_lst:
        length = len(word)

        if length not in out_dict:  ## if this is the first time we have seen this key
            out_dict[length] = [word]
        else:
            out_dict[length].append(word)

        # if length not in out_dict:
        #     out_dict[length] = []
        #
        # out_dict[length].append(word)

    return out_dict








# As part of the code for today, there is a file 'zip-ar.txt' which contains all
# USPS official 5 digits ZIP codes for the state of Arkansas (as of about 2018).

# Read in this data and make:
# -- first, a dictionary keyed the zipcode (as a string) and a list of all cities as the value
# -- then, go the other way -- key is City Name, and value is the list of zipcode


# We will create and run each in the console

def zip_to_city() -> dict[str, list[str]]:
    zip_dict = {}

    with open('zip-ar.txt','r') as f:
        for line in f:
            data = line.strip().split(';')
            zipc = data[0]
            city = data[1]

            if zipc not in zip_dict:
                zip_dict[zipc] = []

            zip_dict[zipc].append(city)

    f.close()

    return zip_dict








