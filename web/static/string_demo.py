# Things with strings

# 1. We can concatenate strings with +
# 2. We can replicate a string with  int * str
#    e.g. 5 * 'hello'

# 3. We can get the character at a particular index
#    with e.g.  'hello'[1]
#    (indices start at 0).

# 4. We can get the length of a string with the len() function

# 5. The last character is at index -1; negative indices count backwards
#    from the end of the string.

# 6. We can get a piece of a string ('slice') by writing
#    string[a:b], which gives us everything starting at index a
#    up to **but not including** index b.


# Keep prompting the user until they enter a valid int.
#
# e.g.
#
# Please enter an int: dog
# Sorry, that is not an int, please try again.
# Please enter an int: five
# Sorry, that is not an int, please try again.
# Please enter an int: 5
#
# Input: prompt is the prompt to display to the user.
# Output: the int entered by the user.
def int_input() -> int:
    q: str = input("Please enter an int: ")
    while not q.isdigit():
        print("Sorry, that is not an int, please try again.")
        q = input("Please enter an int: ")

    return int(q)

