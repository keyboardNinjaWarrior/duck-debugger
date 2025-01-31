from datetime import datetime
import csv
from os import path
from random import randint
from shutil import get_terminal_size

COL = get_terminal_size().columns

with open("duck.txt", "r") as duck:
    for line in duck:
        catPixelRow = line.strip()
        print(catPixelRow.center(COL))

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
        print("ddb:", "quack " * randint(1, 3))
