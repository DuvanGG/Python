
class Vehiculo():
    _color = None
    _ruedas = None
    _puertas = None

    def darColor(self, color):
        self._color = color
    
    def darRuedas(self, ruedas):
        self._ruedas = ruedas
    
    def darPuertas(self, puertas):
        self._puertas = puertas

class Coche(Vehiculo):
    _velocidad = None
    _cilindrada = None

    def darVelocidad(self, velocidad):
        self._velocidad = velocidad
    
    def darCilindrada(self, cilindrada):
        self._cilindrada = cilindrada


miCoche = Coche()
miCoche.darColor("Negro")
miCoche.darRuedas(6)
miCoche.darPuertas(5)
miCoche.darVelocidad(369)
miCoche.darCilindrada(5200)

print("mi coche tiene las siguientes caracteristicas: ", "color:", miCoche._color, 
"ruedas:",miCoche._ruedas, 
"puertas:",miCoche._puertas, 
"velocidad",miCoche._velocidad, 
"cilindrada",miCoche._cilindrada)