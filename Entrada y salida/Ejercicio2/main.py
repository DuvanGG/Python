import pickle

class Vehiculo():
    def __init__(self, velocidad, ruedas):
        self.velocidad = velocidad
        self.ruedas = ruedas

    def __str__(self):
        return f'mi velocidad es {self.velocidad} y tengo {self.ruedas} ruedas'

miCarro = Vehiculo(369, 6)
print(miCarro)

# Serialize
f = open('miObjetoVehiculo', 'wb')
pickle.dump(miCarro, f)
f.close()

# load
f = open('miObjetoVehiculo', 'rb')
carro = pickle.load(f)
f.close()

print(type(carro))
print(carro)