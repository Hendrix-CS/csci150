###############
# analysis.py
#
# for use with
# cleveland-training.csv
# cleveland-testing.csv
#
# CSCI 150 Fall 2015
# Mark Goadrich
########

filename = raw_input("What file would you like to analyze? ")

# Open the file to get the data

fin = open(filename)
data = fin.readlines()[1:]

# Set up the storage of the results

results = {}
results[(True, True)] = 0
results[(True, False)] = 0
results[(False, True)] = 0
results[(False, False)] = 0

for line in data:

    # Loading up each patient into variables
    
    patient = line.strip().split(",")
    age = int(patient[0])
    female = True
    if patient[1] == "False":
        female = False
    chest_pain = patient[2]
    rest_bps = int(patient[3])
    cholesterol = int(patient[4])
    high_fasting_blood_sugar = True
    if patient[5] == "False":
        high_fasting_blood_sugar = False
    rest_ecg = patient[6]
    maximum_heart_rate = int(patient[7])
    exercise_angina = True
    if patient[8] == "False":
        exercise_angina = False
    vessels = int(patient[9])
    heart_disease = True
    if patient[10] == "False":
        heart_disease = False

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

total = results[(True, True)] + results[(False, False)] + \
        results[(True, False)] + results[(False, True)]

correct = results[(True, True)] + results[(False, False)]

# Output the results to the user

print
print "Accuracy on " + filename + " ..."
print "{:.2%}".format(correct / float(total))
print
print "True Positives: \t" + str(results[(True, True)])
print "False Positives:\t" + str(results[(True, False)])
print "True Negatives: \t" + str(results[(False, False)])
print "False Negatives:\t" + str(results[(False, True)])
