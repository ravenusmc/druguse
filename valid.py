#This is the validation file. All functions in this file will serve one purpose to validate the data which the 
#user will be supplying.

def menuValid(choice):
  if choice == 1 or choice == 2 or choice == 3:
    return True
  else:
    return False

def drugSelectionValid(drugSelection):
  if drugSelection == 1 or drugSelection == 2 or drugSelection == 3 or drugSelection == 4 or drugSelection == 5 or drugSelection == 6 or drugSelection == 7:
    return True
  else:
    return False