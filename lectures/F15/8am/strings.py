# String practice
# September 28

# takes a string s as input
# prints the characters of s, one per line
def explode(s):
    index = 0
    while index < len(s):
        print s[index]
        index = index + 1

def main():
    the_str = raw_input("What string would you like to explode today? ")
    explode(the_str)
