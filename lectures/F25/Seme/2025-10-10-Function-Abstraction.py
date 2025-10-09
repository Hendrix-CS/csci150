import random

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

#############################################################
#############################################################
# Example # NOT YET MODULARIZED
#
import random

print("Welcome to Roulette, the simplest Casino Table Game!")
print()
print("You will start with a stake of $100.")
print("You can place any size bet -- whole dollar amounts -- up to your stake.")
print("There are 38 possible slots -- the numbers 1 - 36, and 0, and 00.")
print()
print("Note that 0 and 00 are not considered even!")
print()
print()
print("You can bet on any of the following:")
print()
print("1. Evens (pays 1:1)")
print("2. Odds (pays 1:1)")
print("3. 1st 12 (pays 2:1)")
print("4. 2nd 12 (pays 2:1)")
print("5. 3rd 12 (pays 2:1)")
print("6. Quit")
print()
print()
input('Press "Enter" to start')

stake = 100

cont = True
while cont:
    print(f'Your current stake is ${stake}.')
    succ = False
    while not succ:
        choice = input('What type of bet would you like to make? (1-6): ')
        if choice.isdigit() and 1 <= int(choice) <= 6:
            succ = True
            choice = int(choice)
        else:
            print("You can bet on any of the following:")
            print("1. Evens (pays 1:1)")
            print("2. Odds (pays 1:1)")
            print("3. 1st 12 (pays 2:1)")
            print("4. 2nd 12 (pays 2:1)")
            print("5. 3rd 12 (pays 2:1)")
            print("6. Quit")


    if choice < 6:

        succ = False
        while not succ:
            bet = input(f'Your stake is ${stake}. How much do you want to bet? ')
            if bet.isdigit() and 1 <= int(bet) <= stake:
                succ = True
                bet = int(bet)
            else:
                print(f"Please bet in whole dollar amounts, between 1 and {stake}.")

        roll = random.randint(0,37)
        roll_str = str(roll)
        if roll_str == "37":
            roll_str = "00"

        print(f'A {roll_str} was rolled.')
        if choice == 1:
            if roll > 0 and roll % 2 == 0:
                win = True
                print("You win!")
                stake = stake + bet
            else:
                win = False
                print("You lose!")
                stake = stake - bet

        elif choice == 2:
            if roll < 37 and roll % 2 == 1:
                win = True
                print("You win!")

                stake = stake + bet
            else:
                win = False
                print("You lose!")
                stake = stake - bet

        elif choice == 3:
            if 1 <= roll <= 12:
                win = True
                print("You win!")
                stake = stake + 2 * bet
            else:
                win = False
                print("You lose!")
                stake = stake - bet

        elif choice == 4:
            if 13 <= roll <= 24:
                win = True
                print("You win!")
                stake = stake + 2 * bet
            else:
                win = False
                print("You lose!")
                stake = stake - bet

        elif choice == 5:
            if 25 <= roll <= 36:
                win = True
                print("You win!")
                stake = stake + 2 * bet
            else:
                win = False
                print("You lose!")
                stake = stake - bet



        if stake <= 0:
            print("You have run out of money!")
            cont = False
    else:
        print("Thank you for playing!")
        cont = False

print(f"You finished with a total of ${stake}.")