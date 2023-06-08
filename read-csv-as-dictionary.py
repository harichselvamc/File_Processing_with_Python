# A module for csv
import csv

# Open file for reading
with open("people.csv") as file:
    # create reader
    result = csv.DictReader(file)

    # loop over data
    for line in result:
        print(line)