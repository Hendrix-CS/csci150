tank_size = float(input("How many gallons does your tank hold? "))
mpg = float(input("What is your car's miles per gallon? "))

total_driven = 0.0
fuel_in_tank = tank_size
while fuel_in_tank > 0:
    refuel = input("Do you want to refuel? (yes/no)")
    if refuel == 'yes':
        fuel_in_tank = tank_size
    else:
        distance = float(input("How many miles will you drive? "))
        fuel_use = distance / mpg
        if fuel_use > fuel_in_tank:
            distance = fuel_in_tank * mpg
            fuel_use = fuel_in_tank
        fuel_in_tank -= fuel_use
        total_driven += distance
        print(f"You burned {fuel_use} gallons driving {distance} miles.")
    print(f"You have {fuel_in_tank} gallons left.")
print(f"You are out of fuel. You drove {total_driven} miles.")