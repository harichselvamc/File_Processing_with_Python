# Data processing module
import pandas as pd

# To parse json
import json

# The data
data = [['Alex',33], ['Alice',25], ['Bob', 91]]

# Panda always uses data frames
df = pd.DataFrame(data, columns=['Name','Age'])

# Convert data frame to json
df.to_json('example.json')