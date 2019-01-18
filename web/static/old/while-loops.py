# 17 Feb 2016
# While loops

# Idea: repeat some code as long as some condition is true.

#Syntax:

# while <boolean expression>:
#    stuff

# if executes body 0 or 1 time
# while executes body any number of times (possibly zero)

# Examples.

cur_num = 1
while cur_num <= 10:
    print cur_num
    cur_num = cur_num + 1

# Usually, three main components of using a while loop:
#   1. Initialize some sort of variable to control the loop
#   2. Use some boolean test involving the variable
#   3. At the very end of the loop, update the variable.

# Example 2.  Print "hi", then ask the user if they want to stop.
#   Repeat until user says yes.

answer = 'no'
while answer != 'yes':
    print "hi!!!"
    answer = raw_input('Do you want to stop? ')

wants_to_stop = False
while not wants_to_stop:
    print "hi"
    answer = raw_input('Do you want to stop? ')
    if answer == 'yes':
        wants_to_stop = True
    # wants_to_stop = (answer == 'yes')
