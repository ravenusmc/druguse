import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


def main():
  print("\033c")
  drugs = pd.read_csv('drugs.csv')
  print("1. Alcohol Usage")
  print("2. Marijuana Usage")
  drugSelection = int(input("What do you want to look at? "))
  if drugSelection == 1:
    drugUse = "alcohol-use"
    drug_Graph(drugUse)
  elif drugSelection == 2:
    marijuanaUser()


def drug_Graph(drugUse):
  print("\033c")
  drugs = pd.read_csv('drugs.csv', usecols=["age", drugUse], index_col=['age'])
  drug = drugs[[drugUse]]
  print("Once the graph appears, you must close it to move on")
  input("Press enter to make the graph appear! ")
  plt.show(drug.plot(kind='bar'))


main()














#drugs = pd.read_csv('drugs.csv', usecols=["age", "alcohol-use"], index_col=['age'])
#print(drugs.head())

# alcoholUse = drugs[['alcohol-use']]
# print(use)

# plt.xlabel("Age", fontsize=14)
# plt.ylabel("Freq of Use in past 12 months", fontsize=12)
#test = alcoholUse.plot(kind='bar', title="Alcohol Use")
# plt.show(alcoholUse.plot(kind='bar'))


# Use => Percentage of those in an age group who used marijuana in the past 12 months