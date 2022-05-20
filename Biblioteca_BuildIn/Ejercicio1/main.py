lista = input("Ingresa tu listado de paises separado por comas (,)\n")
lista = lista.split(',')
lista = set(lista)
lista = sorted(lista)

for pais in lista:
    print(pais)