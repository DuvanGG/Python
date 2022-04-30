peso = float(input("Ingrese su peso (kilogramos)"))
estatura = float(input("Ingrese su estatura (metros)"))
IMC = round(peso / (estatura**2),2)
print("Tu indice de masa corporal es: " + str(IMC) )