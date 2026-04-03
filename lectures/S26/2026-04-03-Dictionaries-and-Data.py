# Reminders

# * Quiz Today -- For Loops
# * Final Project Design Document -- due in 2 weeks

# Today, we will look at an example of using dictionaries
# to organize and work with a large data set
#
# In addition to this .py file, there is a .txt file
# on the webpage which contains information about
# zipcode in the US
#
# We will work to understand the data set and
# build a dictionary (or maybe series of dictionaries)
# to help us answer some problems



# We will create a dictionary, keyed on State abbreviation:
#   * value is another dictionary, keyed on City
#       * value is zipcode


def state_city_dict():

    out_dict = {}

    f = open('zipcodes.txt','r')
    for line in f.readlines():
        data = line.split(';')
        state = data[1]
        city = data[2]
        zipc = data[0]

        if state not in out_dict:
            out_dict[state] = {}

        if city not in out_dict[state]:
            out_dict[state][city] = []

        out_dict[state][city].append(zipc)








    f.close()

    return out_dict













