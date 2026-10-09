# Reminders:
#
# Quiz #5 -- Strings today
# Project #2
# -- workshop in class on Monday
# -- due Oct Friday, October 23 (two weeks)



# Function Abstraction

# We have been writing a lot of small functions that do small tasks
#
# Though some of that is because this is an intro level course,
# it is also true that most programming takes place at the small function,
# small individual task level

# Benefits:
# Easier to debug
# Easier to understand
# Often can reuse already-written code
# Easier to modify/update as needed

# Function Abstraction -- big picture: assume each small function
# works correctly. How do the pieces fit together?
# In fact *what* pieces are even needed?

# Modularity -- breaking complicated tasks into small, manageable chunks
# Very rarely should a function be more than 15-20 lines or so long
# (this is not a hard and fast rule)

# Generic Rules:
#
# Each overall program should have a single main()
# main() is the traffic cop -- directs other functions
# main() should *never* return anything (though it might print)
# no other function should *ever* call main
#   -- if you think you have an exception to these rules, ask me

# if main() calls some function f1():
# -- f1() will eventually go back to main:
#    -- if f1() returns a value, that value is only returned to main()
#         (of course, not every function returns something)
#    -- if f1() calls g1(), g1() will eventually go back to f1()
#        -- not to main()
#    -- if g1 calls some h1(),  h1() goes back to g1(), which
#               goes back to f1(), which goes back to main()

# each function should have a single, simple task to complete
# which you should be able to describe in a sentence or so
#
# if you find yourself saying "it calculates area *and* then also calculates..."
#   you really have two functions, almost certainly

############ Possible main for a  game:
# def main():
#     welcome()
#     print_rules()
#     again = True
#     while again:
#         level = choose_level()
#         play_game(level)
#         again = play_again()

# Then, you write each of the individual functions as you go.

# Some things to do / not do:
# You should have *one* function main()
# - it takes in no parameters
# - it does not return anything
# - no function is allowed to call main()
# Map out what you think each function's
# -- primary job is
# -- what, if anything does it need to know (these are the parameters)
# -- what, if anything does it need to return
#    -- a function should return *at most* one thing
#    -- if you think you might have an exception, talk with me!




