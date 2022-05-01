import math

def areaTriangulo(altura, base):
    return (float(base) * float(altura)) / 2

resultadoTriangulo = areaTriangulo(10.5, 18)


def areaCirculo(radio):
    return (math.pi * (radio**2))

resultadoCirculo = areaCirculo(5)

print("El area del triangulo es: ", resultadoTriangulo)
print("El area del circulo es: ", resultadoCirculo)