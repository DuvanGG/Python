class Alumno():
    #Inicializacion
    def inicial(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    #Funcion mostrar datos
    def mostrar(self):
        print(self.nombre)
        print(self.nota)

    #Funcion de para aprobar o reprobar
    def esAprobado(self):
        if self.nota >= 3:
            print("Aprobo! =)")
        else:
            print("Reprobo, =(")

   
alumnoA = Alumno()
alumnoB = Alumno()

alumnoA.inicial("Juan Quintana", 5)
alumnoA.mostrar()
alumnoA.esAprobado()
alumnoB.inicial("Eliza Parra", 2.9)
alumnoB.mostrar()
alumnoB.esAprobado()