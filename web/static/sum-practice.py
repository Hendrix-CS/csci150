# Calculate the sum of the first N odd numbers.
def Main():
    print("We will compute the sum of some odd numbers.")
    n = input("How many odd numbers would you like to add? ")
    count = 0
    odd = 1
total = 0

    while (count != n):
        total = total + odd
        odd = Odd + 1
        count += 1

    print("The sum of the first " + str(n) + " odd numbers is " + str(total) + ".")

main()
