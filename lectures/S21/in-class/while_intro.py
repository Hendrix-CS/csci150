# Repetition in Python!

# while is very similar to if

# syntax for if (review):

# if <condition>:
#   stuff

# 'stuff' gets done 0 or 1 times, depending on the <condition>.

# syntax for while:

# while <condition>:
#   stuff

# 'stuff' gets done 0 or *more* times.
# - checks the condition
# - if condition is true, does 'stuff'
# - then returns to check the condition again
# - etc, keeps doing this until the condition is false.

# Example that counts from 1 to 10:

count = 1
while count <= 10:
    print(count)
    count = count + 1
print('Done')
print(count)

# count = 1
# while count <= 10:
#     count = count + 1
#     print(count-1)
# print('Done')
# print(count)