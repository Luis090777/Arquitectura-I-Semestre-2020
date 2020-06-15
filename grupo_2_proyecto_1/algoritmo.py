def validar_numeros(a,b):

  """
  Validates if a and b are numbers, if they aren't, the program stops
  Input: a and b are numbers or text
  Output: True if the a and b are numbers, False if a or/and b aren't numbers
  """

  if type(a) != int: #If a isn't a integer, return False
    return False

  elif type(b) != int: #If b isn't a integer, return False
    return False

  elif a > 255 and b > 255: #If a or b are out of the number range of 8-bits, return False
    return False

  else: #If both are valid numbers, return True
    return True

    
def main():

  """
  We will use this if we have to ask for the numbers
  a = int(input("intruduzca el primer numero a multiplicar: \n" ))

  b = int(input("intruduzca el segundo numero a multiplicar: \n"))
  """
  a = 3
  b = 6
    
  if (validar_numeros(a,b) != True): #Calls validar_numeros function
  		print("Ingrese solo números")
    
  else: #Prints the result of the multiplicated numbers
    print ""
    
main()