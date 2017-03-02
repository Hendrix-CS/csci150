# For loops

def explode_str(s):
    index = 0
    while index < len(s):
        print(s[index])
        index += 1

# The above is too low-level: lots of things to get wrong!

def explode_str2(s):
    for c in s.lower():
        print(c)

# Syntax:
# for <var> in <sequence expression>:
#    ... stuff using <var>

animals = ['chicken', 'rabbit', 'duck', 'chupacabra', 'deer']

# for animal in animals:
#    print ("And on this farm he had a " + animal + "...")

# With a normal for loop we don't get access to the indices.
# But we can do this:

# for i in range(len(animals)):
#     print ("At index " + str(i) + ": " + animals[i])



# For loop practice

# Input: string s, character c
# Output: number of times c occurs in s.
def count(s, c):
    count = 0
    for i in s:
        if i==c:
            count += 1
    return count    

# Input: string s, character c
# Output: index of the first occurrence of c in s, or -1
#   if it does not occur.
def find(s, c):
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            index = i
            return index
        

# Input: string s, character c
# Output list of all the indices where c occurs.
# Example: find_all("hello", 'l') == [2,3]
def find_all(s, c):
    pass

