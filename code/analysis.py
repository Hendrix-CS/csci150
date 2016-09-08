###############
# analysis.py
#
# for use with
# cleveland-training.csv
# cleveland-testing.csv
#
# CSCI 150 Fall 2016
# Mark Goadrich
# Updated for Python 3.5 by Gabriel Ferrer
########

filename = input("What file would you like to analyze? ")

# Open the file to get the data

fin = open(filename)
data = fin.readlines()[1:]

# Set up the storage of the results

results = {(a, b):0 for a in (True, False) for b in (True, False)}

for line in data:

    # Loading up each patient into variables
    
    patient = line.strip().split(",")
    age = int(patient[0])
    female = (patient[1] == "True")
    chest_pain = patient[2]
    rest_bps = int(patient[3])
    cholesterol = int(patient[4])
    high_fasting_blood_sugar = (patient[5] == "True")
    rest_ecg = patient[6]
    maximum_heart_rate = int(patient[7])
    exercise_angina = (patient[8] == "True")
    vessels = int(patient[9])
    heart_disease = (patient[10] == "True")

    ##################################
    # BEGIN PREDICTION CODE
    ##################################

    prediction = True
    
    ##################################
    # END PREDICTION CODE
    ##################################

    # Saving the results
    
    results[(prediction, heart_disease)] += 1

# Calculating the accuracy on all patients

total = sum(results[(a, b)] for a in (True, False) for b in (True, False))
correct = results[(True, True)] + results[(False, False)]

# Output the results to the user

print()
print("Accuracy on " + filename + " ...")
print("{:.2%}".format(correct / float(total)))
print()
for (a, b) in ((True, True), (True, False), (False, False), (False, True)):
    print("True " if a == b else "False", 
          "Positives:" if a else "Negatives:", 
          "\t" + str(results[(a, b)]))
