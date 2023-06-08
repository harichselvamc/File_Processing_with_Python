# Load data analysis module
import pandas as pd 

# define data
name = ["Alice","Bob"]
subjects = ["Math","English"]
marks = [9,10,]

# create dict
dictionary = { 'name': name, 'subjects': subjects, 'marks': marks}

# create dataframe
df = pd.DataFrame(dictionary)

# save to csv
df.to_csv("school.csv")