# Load csv module
import csv

# data
mydict = [{ 'name': 'Alice', 'age': 18},
          { 'name': 'Bob', 'age': 25}]

header = ['name', 'age']

# Open file for writing 
with open('people.csv', 'w') as csvfile:
    # create a writer
    writer = csv.DictWriter(csvfile, fieldnames= header)

    # writes the data to the file
    writer.writeheader()
    writer.writerows(mydict)