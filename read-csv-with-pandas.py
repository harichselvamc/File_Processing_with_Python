# Load data analysis module
import pandas as pd

# Read csv file into pandas data frame
df = pd.read_csv('fruit.csv')

# converts data frame to lists
mylists = df.values.tolist()

# loop over the lists
for lst in mylists:
    print(lst)