#Número Positivo o Negativo
#Pide un número al usuario. Di si es positivo, negativo o si es cero.
def Positivo(prompt):
    while(True):
        try:
            numero = float(input(prompt))
            return numero
           
        except ValueError:
            print("El numero es invalido    ")
            
Cero = Positivo("Ingrese un numero: ")
if Cero >0:
    print("El numero es postivo:    ")
elif Cero<0:
    print("El numero es negativo:   ")
else:
    print("El numero es cero:")

