
class Vehiculo:
    color = "Negro"
    ruedas = 6
    puertas = 5

class Coche(Vehiculo):
    velocidad = 963
    cilindrada = 369

miCoche = Coche()
print("mi coche es de color: ", miCoche.color)
print("mi coche tiene ", miCoche.ruedas,"ruedas")
print("mi coche tiene", miCoche.puertas,"puertas")
print("mi coche tiene una velocidad de:", miCoche.velocidad)
print("mi coche tiene una cilindrada de:", miCoche.cilindrada)