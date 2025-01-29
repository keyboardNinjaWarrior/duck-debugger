from datetime import datetime
import csv

with open("log.csv", 'a') as log:
    csvlog = csv.writer(log)
    csvlog.writerow(["time", "text"])
    while (True):
        user_input = input("You: ")
        if user_input == ":exit":
            break
        csvlog.writerow([datetime.now().strftime("%d-%m-%Y %H:%M:%S"), user_input])
