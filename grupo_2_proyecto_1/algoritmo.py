def sumador_binario(numero_a, numero_b):  
  """
    Binary addition.
    Input: numero_a and numero_b are a tuple with one number each.
    Output: Will return the addition as a tuple
 
  """

  # Compare the size of the 2 tuples and add make them equal
  tamanio = len(numero_a)-len(numero_b)

  if tamanio > 0:
        # Add 0's as necessary to equal the size of numbers
    numero_b = ((0,) * tamanio) + numero_b
        
  elif tamanio < 0:
        
        #Add 0's as neccessary to equal the size of numbers
    numero_a = ((0,) * (-tamanio)) + numero_a # We use "-tamanio" to convert tamanio to a positive number
  
  carry = 0
  arreglo_bits = [0]*(len(numero_a)+1) # Final array with 0's and 1's

  # Go through the array adding 0's or 1's according to the division or the multiplication
  for j in reversed(range(0, len(numero_a))):

    # Starts the cycle to add the bits of both of the tuples
    # Add the numbers from the tuples and divide them by 2, to get 0 or 1 depending on the
    # upcoming bits
    division_entera = (numero_a[j] + numero_b[j] + carry) // 2

    # Assign the previous operation to the current positions in the array, because we are
    # adding bits, so we have to get 0's and 1's and in this case
    # j+1 because the array has one more position than the tuples.
    arreglo_bits[j+1] = (numero_a[j] + numero_b[j] + carry) - 2*division_entera

    # Takes the value of division_entera to keep doing the
    # multiplication correctly in the next iteration
    carry = division_entera 
                            
          
    arreglo_bits[0] = carry # Assign the carry to the first position of the array, because                          # it's a carry
  

  if arreglo_bits[0] == 0: #When arreglo_bits doesn't increase the bits of the original numbers, eliminates the extra 0

    arreglo_bits.remove(0) 
  return tuple(arreglo_bits)


def corrimiento_izquierda(numero_a,bits):
  """
  Make a shift left of the upcoming bits by n bits.
  Input: numero_a is one of the numbers and bits is the amount of bits that we are going
  to shift, usually 1
  Output: Returns the tuple shifted by n bits.
  """

  # If type of numero_a is different than a tuple, it will return an empty tuple as output
  # It can also be seeing as a "True" 
  if type(numero_a) != tuple:
    return ()
  
  # If it is tuple, it will return the tuple shifted by n bits
  # In python we can use "<<" to make a shift left, but we wanted to do it in binary, so
  # we are using a step by step operation to add 0's to the tuple
  else:
    return numero_a + (0,) * bits
  
  
def dec_a_bin(n):

  """
  Converts the given number from decimal to binary
  Input: n is a base 10 number
  Output: A string with the binary number
  """
  
  
  if n < 0: #If the number is bigger than 0
    return "Debe ser un número mayor a 0"
    
  elif n == 0: #If the number is equal to zero
    return "0"
    
  else: #If n is a valid number, add the 0 or 1 at the verified position and call this function again
    return dec_a_bin(n//2) + str(n%2)
        
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
