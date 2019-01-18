def div_three_five(t):
    if t == []:
        return True
    else:
        candiv = div_three_five(t[1:])
        if (candiv and (t[0] % 3 == 0 or t[0] % 5 == 0)):
            return True
        else:
            return False

# Input: s (string)
# Output: len(s)
def length(s):
    if s == '':
        return 0
    else:
        #  ... assume length(s[1:]) works
        # then the length of s is one more than that.

        return 1 + length(s[1:])

# Write a function
##prev_up
##that takes an alphabetic string as a parameter
##and returns a dictionary, where the keys are letters of the alphabet and
##the values are the number of times each letter was immediately preceded
##by the previous letter in the alphabet (where
##"s"
##is preceded by
##"r"
##, etc.,
##and we count
##"a"
##as being preceded by
##"z"
##) if this number is 1 or more.
##For example:
##•
##prev_up("defenders")
##→
##{’s’: 1, ’f’: 1, ’e’: 2}
##•
##prev_up("misunderstanders")
##→
##{’t’: 1, ’s’: 2, ’e’: 2}
##•
##prev_up("understudy")
##→
##{’t’: 1, ’s’: 1, ’e’: 1, ’u’: 1}

def prev_up(s):

    prev_counts = {}

    # Loop over index 1 .. end
    for i in range(1, len(s)):

        # If char at index i is preceded by the previous letter
        # of the alphabet...
        if (ord(s[i]) == 1 + ord(s[i-1])):

            # See if it's already in the dictionary or not,
            # increment the count if it is, and initialize the count
            # to 1 if it isn't yet.
            if s[i] in prev_counts:
                prev_counts[s[i]] += 1
            else:
                prev_counts[s[i]] = 1

    return prev_counts


def stuck(d):
    stuck_cities = []
    
    for start in d:  # For each starting city
        for dest in d[start]:  # For each destination
            
            # dest is not a key, i.e. not a starting city
            # and not already in stuck_cities
            if dest not in d and dest not in stuck_cities:    
                stuck_cities.append(dest)

    return stuck_cities






    

    
