from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def sumaImpar(lista):
    #lambda: funcion anonima
    impar = filter(lambda x: x % 2, lista)
    print(f'la lista de impares es: {list(impar)}')

    suma = reduce(lambda x, y: x + y, lista)
    print(f'la suma es: {suma}')

sumaImpar(lista)
