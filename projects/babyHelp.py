print("Welcome to the baby helper. Answer \"yes\" or \"no\" to each question.")
sleep = input("Is your baby sleeping?")
if sleep == "yes":
    print("Congratulations, do not disturb!")
else:
    cry = input("Is she crying?")
    if cry == "no":
        print("Great, leave her alone.")
    else:
        diaper = input("Does she need a diaper change?")
        if diaper == "yes":
            wet = input("Is the diaper merely wet?")
            if wet == "yes":
                print("Take off the wet diaper, throw it out, and put on a dry one")
            else:
                print("Take off the dirty diaper and throw it out")
                print("Clean her thoroughly and put on a clean diaper")

            full = input("Is the diaper bin full?")
            if full == "yes":
                print("Take out the filled bag and replace it with an empty one.")
                print("Place the filled bag in the garbage can outside.")
        
        cold = input("Is she cold?")
        if cold == "yes":
            ac = input("Is the AC running?")
            if ac == "yes":
                print("Turn it off!")
            else:
                print("Dress her in warmer clothing.")

        cry = input("Is she still crying?")
        if cry == "yes":
            print("She must be hungry. Feed her a bottle.")

        print("At this point, she should be okay. If not, I am at a loss...")
