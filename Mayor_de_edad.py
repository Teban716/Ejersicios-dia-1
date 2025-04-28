#Mayor de Edad
#Pide al usuario su edad. Si tiene 18 años o más, imprime "Eres mayor de edad". Si no, imprime "Eres menor de edad".

def pedir_numero_positivo(prompt):
    while(True):
        try:
            numero = int(input(prompt))
            if numero :
                return numero
            else:
                print("Ingresar tu edad:    ")
        except ValueError:
            print("El numero es invalido    ")
            
Edad=pedir_numero_positivo("Ingrese la Edad:    ")

if Edad >= 18:
    print("Eres mayor de edad")
elif Edad>1:
    print("Eres menor de edad")
else:
    input("Escribe un numero valido")