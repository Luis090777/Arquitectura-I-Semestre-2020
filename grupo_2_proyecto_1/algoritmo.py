def validar_numeros(a,b):

    if type(a) != int:
        print("1111")
        print("Ingrese solo números")
        return False

    elif type(b) != int:
        
        print("Ingrese solo números")
        return False

    elif a > 255 and b > 255:
        return False

    else:
        return True


def main():

    '''
    We will use this if we have to ask for the numbers
    a = int(input("intruduzca el primer numero a multiplicar: \n" ))

    b = int(input("intruduzca el segundo numero a multiplicar: \n"))
    '''
    a = 3
    b = 6
    
    if validar_numeros(a,b) != True:
        print("Ingrese solo números")
    
    else:
        return None
        # Aquí va la función de multiplicar

print(main())