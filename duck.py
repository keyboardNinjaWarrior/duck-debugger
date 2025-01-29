from datetime import datetime
import csv

# print(datetime.now())

with open("log.csv", 'a') as log:
    csvlog = csv.writer(log)
    csvlog.writerow(["time", "text"])
