# While loops

# while condition:
#     body

# if the condition is true,
#    execute the body and then check the condition again
# keep doing this until the condition is false.

n = 0              # 1. Initialize a variable
while n <= 10:     # 2. Write the condition using that variable
    print n     
    n = n + 1      # 3. Modify the variable inside the loop
                   #    (otherwise you will have an infinite loop)
                   #    (Ctrl-C if you are stuck in a loop) 

print "Done!"
