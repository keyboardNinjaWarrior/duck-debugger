from datetime import datetime
import csv
from os import path

filePath = "log.csv"

with open(filePath, 'a') as log:
    csvLog = csv.writer(log)
    readLog = open(filePath, "r")
    while (True):
        userInput = input("You: ")
        if userInput == ":q":
            break
        csvlog.writerow([datetime.now().strftime("%d-%m-%Y %H:%M:%S"), userInput])
