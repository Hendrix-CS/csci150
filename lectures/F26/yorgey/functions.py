# Functions!
#
# From now on, everything should be in a function!
#
# Benefits of using functions?
#
# 1. Call function multiple times instead of copy-pasting code
# 2. Better organization, documentation about variables
# 3. Easier to adapt to multiple purposes/situations
# 4. Organization/outline helps with human comprehension of code

# Functions can be used to organize a program hierarchically - a top-level main() function
# breaks up the task into smaller tasks by calling some functions, which themselves break up
# their tasks into smaller tasks, etc.

# Do NOT do this, having each function call the function that should happen next.
# def main():
#     do_thing1()
#
# def do_thing1():
#     do some stuff
#     do_thing2()
#
# def do_thing2():
#     do some more stuff
#     do_thing3()
#
# def do_thing3()
#     do lots of stuff

# Instead, do this:
# def main():
#     do_thing1()
#     do_thing2()
#     do_thing3()
#
# def do_thing1():
#     do some stuff
#
# def do_thing2():
#     do some more stuff
#
# def do_thing3()
#     do lots of stuff
