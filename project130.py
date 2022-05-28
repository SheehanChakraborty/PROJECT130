import pandas as pd 
import csv

df = pd.read_csv("PROJECT128.csv")
print(df.columns)
print(df.shape)
del df ["Star_name"]
del df ["Distance"]
del df ["Mass"]
print(df.columns)
df.to_csv("c130.csv")