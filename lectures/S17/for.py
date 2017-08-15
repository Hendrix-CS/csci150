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
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1
            
        

# Input: string s, character c
# Output list of all the indices where c occurs.
# Example: find_all("hello", 'l') == [2,3]
def find_all(s, c):
    pass



def oogie(m):
    p = m[0]
    for g in m:
        if g > p:
            p = g
    return p


def yaya(q):
    for y in range(len(q) - 1):
        if q[y] == q[y+1]:
            return True
    return False

def is_sorted(items):
    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            return False
    return True

def pulu(r):
    b = []
    for k in range(r):
        b.append(k ** 3)
    return b













