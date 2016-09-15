#This is the validation file. All functions in this file will serve one purpose to validate the data which the 
#user will be supplying.

def menuValid(choice):
  if choice == 1 or choice == 2:
    return True
  else:
    return False