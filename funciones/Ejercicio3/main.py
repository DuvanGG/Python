anio = 2024

def esBisiesto():
    if anio % 4 == 0 and (anio % 100 == 0) == (anio % 400 == 0):
        print( anio, "SI es un año bisiesto, tiene 366 dias")
    else:
        print(anio, "NO es un año bisiesto, tiene 365 dias")

print(esBisiesto())