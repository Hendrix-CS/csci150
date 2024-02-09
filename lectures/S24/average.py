total = 0
count = 0

n = int(input("Enter a number: "))
while n >= 0:
    total = total + n
    count = count + 1
    n = int(input("Enter a number (-1 to quit): "))

average = total / count
print(f"The average of the {count} numbers you entered is {average}.")