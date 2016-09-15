import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

drugs = pd.read_csv('drugs.csv', usecols=["age", "alcohol-use"], index_col=['age'])
#print(drugs.head())

alcoholUse = drugs[['alcohol-use']]
# print(use)

# plt.xlabel("Age", fontsize=14)
# plt.ylabel("Freq of Use in past 12 months", fontsize=12)
test = alcoholUse.plot(kind='bar', title="Alcohol Use")
plt.show(test)


# Use => Percentage of those in an age group who used marijuana in the past 12 months