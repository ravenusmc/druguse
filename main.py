#This is the main file of the project. 
#Importing the libraries that will be used:
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from valid import *

#This is the first function in the program which will simply greet the user. 
def main():
  print("\033c")
  print("---------~~~~----------")
  print("--Welcome to Drug Use--")
  print("----~~~---------~~~----")
  input("Hit enter to continue ")
  menu()

#This is the first menut in the program which will ask the user what they want to do. 
def menu():
  print("\033c")
  print("Main Menu")
  print("1. Look at Data")
  print("2. Information about this program")
  print("3. Quit")
  choice = int(input("What would you like to do? "))
  while not menuValid(choice):
    print("That is not a valid selection")
    choice = int(input("What would you like to do? "))
  if choice == 1:
    dataMenu()
  elif choice == 2:
    information()
  elif choice == 3:
    print("Thank you for using the program.")
    print("I hope that you stop by soon!")
    input("Press enter to exit ")

#This function will be the menu for the user to select what they want to look at.
def dataMenu():
  print("\033c")
  drugs = pd.read_csv('drugs.csv')
  print("1. Alcohol Usage")
  print("2. Marijuana Usage")
  print("3. Cocaine Usage")
  print("4. Heroin Usage")
  print("5. Hallucinogen Usage")
  print("6. Inhalant Usage")
  print("7. Pain Releiver Usage")
  drugSelection = int(input("What do you want to look at? "))
  while not drugSelectionValid(drugSelection):
    print("What is not a valid selection!")
    drugSelection = int(input("What do you want to look at? "))
  if drugSelection == 1:
    drugUse = "alcohol-use"
    drug_Graph(drugUse)
  elif drugSelection == 2:
    drugUse = "marijuana-use"
    drug_Graph(drugUse)
  elif drugSelection == 3:
    drugUse = "cocaine-use"
    drug_Graph(drugUse)
  elif drugSelection == 4:
    drugUse = "heroin-use"
    drug_Graph(drugUse)
  elif drugSelection == 5:
    drugUse = "hallucinogen-use"
    drug_Graph(drugUse)
  elif drugSelection == 6:
    drugUse = "inhalant-use"
    drug_Graph(drugUse)
  elif drugSelection == 7:
    drugUse = "pain-releiver-use"
    drug_Graph(drugUse)

#I originally had numerous functions for each drug but refractured my code to only have one function! This one function
#will display the bar graph for the drug data. 
def drug_Graph(drugUse):
  print("\033c")
  drugs = pd.read_csv('drugs.csv', usecols=["age", drugUse], index_col=['age'])
  drug = drugs[[drugUse]]
  print("Once the graph appears, you must close it to move on")
  input("Press enter to make the graph appear! ")
  plt.show(drug.plot(kind='bar', title = drugUse, figsize=(12,8)))
  dataMenu_OrQuit()

#This function simply tells the user some basic information about this program-specifically focusing on the data
#aspect. 
def information():
  print("\033c")
  print("The data used in this project came from the FiveThirtyEight github repo.")
  print("This project specifically looks at the percentage of people, in an age group,")
  print("Who used the drug in the past 12 months.")
  print("That is all!")
  dataMenu_OrQuit()


### Non-Critical program functions below here.  

#This function will be used over and over again through out the program that allows the user to return to the main menu
#or to quit.
def dataMenu_OrQuit():
  print("1. Return to data Menu")
  print("2. Quit")
  choice = int(input("What is your option? "))
  while not menuValid(choice):
    print("That is not a valid selection!")
    choice = int(input("What is your option? "))
  if choice == 1:
    dataMenu()
  elif choice == 2:
    print("Thank you for using the program!")
    print("I hope that you enjoyed it!")


main()





