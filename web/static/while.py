#
# Syntax of while loops (repetition):
#
# while <condition>:
#    <statement>
#    <statement>
#    ...
#
# Checks condition:
#   - if false, skip body
#   - if true, execute body and then check condition again, etc.

x = 3
while x < 10:
    x = x + 1
    print(x)

print("Now x is " + str(x))

# Program should:
#   1. print "hi"
#   2. ask user "do you want to quit?"
#   3. stop if user inputs 'yes', otherwise, repeat.

# quit = 'GO!'
#
# while quit != 'yes':
#     print("hi")
#     quit = input("Do you want to quit? ")

# print("hi")
# while input("Do you want to quit? ") != 'yes':
#     print("hi")

# print("hi")
# quit = input("Do you want to quit? ")
# while quit != 'yes':
#     print("hi")
#     quit = input("Do you want to quit? ")

# while input("hi\nDo you want to quit? ") != 'yes': pass

# done is a "sentinel variable" -- boolean that controls loop
done = False
while not done:
    print("hi")
    quit = input("Do you want to quit? ")
    if quit == 'yes':
        done = True

# Typical 3 components of a while loop:
#   1. initialize loop control variable
#   2. condition using loop control variable
#   3. update the loop control variable at the *end* of the body.