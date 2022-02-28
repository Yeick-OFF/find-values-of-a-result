import random

numero1 = 0
numero2 = 0
print("Encontrar operacion de 2 resultados")

intentos = 0
resultado = 15
resultado1 = 8
axis = resultado

while((numero1 * numero2) != resultado or (numero1 + numero2) != resultado1 and (numero1 * numero2) != resultado or (numero1 + numero2) != resultado1):
    numero1 = random.randint(-10,20)
    numero2 = random.randint(-10,20)
    
    
    if(numero1 * numero2 == resultado and numero1 + numero2 == resultado1):
        print(numero1)
        print(numero2)
        print("------")
    
    intentos = intentos + 1

    if(intentos == 10000):
        resultado = resultado1
        resultado1 = axis
