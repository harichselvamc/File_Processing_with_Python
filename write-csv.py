# Load csv module
import csv 

# header
header = ['Fruit', 'Price']

# data
rows = [ ['Apple', 5],
         ['Berry', 6],
         ['Lemon', 1],
         ['Melon', 9]]

# open file for writing
with open('example.csv', 'w') as csvfile:
    # create the file writer
    csvwriter = csv.writer(csvfile)

    # write data
    csvwriter.writerow(header)
    csvwriter.writerows(rows)
