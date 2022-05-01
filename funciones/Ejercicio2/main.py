numero = 457

def esPrimo(numero):
    esUnNumPrimo = True
    for i in range(2, numero):
        if numero % i == 0:
            esUnNumPrimo = False
    return esUnNumPrimo

if esPrimo(numero) == True:
    print(numero, " SI es un numero primo")
else:
    print(numero, " NO es un numero primo")