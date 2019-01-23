# CSCI 150, Spring 2016
# Drake Equation
# Our first program!

# Tell the user about the Drake equation
print """This is a program to compute the Drake equation.
Blah blah blah.
"""

# Prompt the user for R* (rate of star formation)
r_star_str = raw_input("Please enter R*, the rate of star formation: ")
r_star = float(r_star_str)

# r_star = float(raw_input("Please enter R*, the rate of star formation: "))

# Prompt the user for Fp (fraction that have planets)
f_p = float(raw_input("Please enter f_p, the fraction of stars that have planets: "))

# ... prompt for all the other variables

# Calculate N
N = r_star * f_p

# Display N to the user
print "The value of N is", N
