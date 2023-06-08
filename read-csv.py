# Import module
import csv

# Open the file
with open('people.csv') as csvDataFile:

    # Read CSV file
    csvReader = csv.reader(csvDataFile)
    
    # Read every row as a Python list
    for row in csvReader:
        print(row)
