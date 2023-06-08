# Load data analysis module
import pandas as pd 
# Required for excel
import openpyxl

# Create data frame
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],
                   index=['one','two','three'], columns=['a','b','c'])

print(df)

# Convert data frame to Excel
df.to_excel('pandas.xlsx', sheet_name='pandas')