def corrimiento_izquierda(numero_a,bits):
  """
  Make a shift left of the upcoming bits by n bits.
  Input: numero_a is one of the numbers and bits is the amount of bits that we are going
  to shift, usually 1
  Output: Returns the tuple shifted by n bits.
  """

  # If type of numero_a is different than a tuple, it will return an empty tuple
  # It can also be seeing as a "True"
  if type(numero_a) != tuple:
    return ()
  
  # If it is tuple, it will return the tuple shifted by n bits
  # In python we can use "<<" to make a shift left, but we wanted to do it in binary, so
  # we are using a step by step operation to add 0's to the tuple
  else:
    return numero_a + (0,) * bits

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