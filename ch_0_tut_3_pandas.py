# Install using `conda install -c anaconda pandas`
# import package
import pandas as pd

df = pd.read_csv('countries.csv')

# -----------------------------------------------------------
# First 5 rows (by default)
# print(df.head())
# print(df.head(10))		# first 10 rows

#------------------------------------------------------------
# # Last 5 rows (by default)
# print(df.tail())
# print(df.tail(15))		# last 15 rows

#------------------------------------------------------------
# # dataframe for 'China' population
df_china = df[df["country"] == 'China']
print(df_china)