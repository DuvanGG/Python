numInicio = int(input("Ingresa el numero de inicio "))
numFinal = int(input("Ingresa el numero de fin "))
numeros = []

if numFinal < numInicio:
    numeros.append("Ingresa un numero mayor al inicial")
    

for num in range(numInicio, numFinal):
    if num % 2 != 0:
        numeros.append(num)

print("La lista de numeros impares es: ", numeros)