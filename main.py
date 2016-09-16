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
  print("2. Quit")
  choice = int(input("What would you like to do? "))
  while not menuValid(choice):
    print("That is not a valid selection")
    choice = int(input("What would you like to do? "))
  if choice == 1:
    dataMenu()
  elif choice == 2:
    print("Thank you for using the program.")
    print("I hope that you stop by soon!")
    input("Press enter to exit ")

#This function will be the menu for the user to select what they want to look at.
def dataMenu():
  print("\033c")
  drugs = pd.read_csv('drugs.csv')
  print("1. Alcohol Usage")
  print("2. Marijuana Usage")
  drugSelection = int(input("What do you want to look at? "))
  while not drugSelectionValid(drugSelection):
    print("What is not a valid selection!")
    drugSelection = int(input("What do you want to look at? "))
  if drugSelection == 1:
    alcoholUser()
  elif drugSelection == 2:
    marijuanaUser()

#This function will allow the user to look at alcohol usage. 
def alcoholUser():
  print("\033c")
  drugs = pd.read_csv('drugs.csv', usecols=["age", "alcohol-use"], index_col=['age'])
  alcoholUse = drugs[['alcohol-use']]
  print("Once the graph appears, you must close it to move on")
  input("Press enter to make the graph appear! ")
  plt.show(alcoholUse.plot(kind='bar'))
  dataMenu_OrQuit()

#This function will allow the user to look at alcohol usage. 
def marijuanaUser():
  print("\033c")
  drugs = pd.read_csv('drugs.csv', usecols=["age", "marijuana-use"], index_col=['age'])
  marijuanaUse = drugs[['marijuana-use']]
  print("Once the graph appears, you must close it to move on")
  input("Press enter to make the graph appear! ")
  plt.show(marijuanaUse.plot(kind='bar'))
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





