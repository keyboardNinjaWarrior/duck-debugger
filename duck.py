from datetime import datetime
import csv
from os import path

filePath = "log.csv"

with open(filePath, "a") as log:
    csvLog = csv.writer(log)
    with open(filePath, "r") as readLog:
        if readLog.readline() == "":
            csvLog.writerow(["time", "text"])
    while (True):
        userInput = input("You: ")
        if userInput == ":q":
            break
        csvLog.writerow([datetime.now().strftime("%d-%m-%Y %H:%M:%S"), userInput])
