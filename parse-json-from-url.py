# To load data from URL
import requests

# data processing module
import pandas as pd 

# the API url with json data
url = "https://jsonplaceholder.typicode.com/todos/3"

# get data
r = requests.get(url)

x = r.json()
print(x)

# Load json data as pandas data frame
df = pd.json_normalize(r.json())
print(df)