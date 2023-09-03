import sys
import pandas as pd

def check_prediction(filename: str, predict, required_accuracy: float):
    # Open the file to get the data

    data = pd.read_csv("cleveland-" + filename + ".csv")

    # Set up the storage of the results

    results = [[0, 0],
               [0, 0]]

    for index, row in data.iterrows():

        # Make a prediction

        prediction = predict(row["age"], row["female"], row["chest_pain"], row["rest_bps"],
                             row["cholesterol"], row["high_fasting_blood_sugar"], row["rest_ecg"],
                             row["maximum_heart_rate"], row["exercise_angina"], row["vessels"])

        # Saving the results

        results[1 - int(prediction)][1 - row["heart_disease"]] += 1

    correct = results[0][0] + results[1][1]
    total = len(data)
    accuracy = correct/float(total)

    if accuracy >= required_accuracy:
        print("{:.2%}".format(accuracy) + " accuracy (required: " + "{:.2%}".format(required_accuracy) + "), good job!")
    else:
        print("{:.2%}".format(required_accuracy) + " accuracy is required, but you only achieved " + "{:.2%}".format(accuracy))
        sys.exit(1)
