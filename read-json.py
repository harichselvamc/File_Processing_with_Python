# Load data analysis module
import pandas as pd 

# Load json data
import json

# Read json as data frame
df = pd.read_json('example.json')
print(df)