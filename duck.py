from datetime   import datetime
import csv
from pathlib    import Path
from os         import path
from random     import randint
from shutil     import get_terminal_size

COL = get_terminal_size ().columns

# prints the duck on the screen
with open ("duck.txt", "r") as duck:
    for line in duck:
        duckPixelRow = line.strip ()
        print (duckPixelRow.center(COL))

filePath = Path ("log.csv")
headers = ["time", "text"]

# establish file headers
if not path.exists (filePath):
    filePath.touch ()
    with open (filePath, "a") as logs:
        writelog = csv.writer (logs)
        writelog.writerow (["time", "text"])

with open (filePath, "a") as logs:
    writelog = csv.writer (logs)
    print()

    while (True):
        userInput = input("You: ")
        
        # quit condition
        if userInput == ":q":
            break
        
        writelog.writerow([datetime.now().strftime("%d-%m-%Y %H:%M:%S"), userInput])
        print("ddb:", "quack " * randint(1, 3))
