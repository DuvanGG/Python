import sqlite3

# abrir base de datos
conn = sqlite3.connect('mibase.db')
# cursosr para enviar los comandos (iterador)
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Alumnos(Id INT, Nombre TEXT, Apellido TEXT)')

cursor.execute('INSERT INTO Alumnos (Id, Nombre, Apellido) VALUES (1, "Jose", "Rodriguez")')
cursor.execute('INSERT INTO Alumnos (Id, Nombre, Apellido) VALUES (2, "Antonia", "Garcia")')
cursor.execute('INSERT INTO Alumnos (Id, Nombre, Apellido) VALUES (3, "Juan", "Cipriano")')
cursor.execute('INSERT INTO Alumnos (Id, Nombre, Apellido) VALUES (4, "Maria", "DB")')
cursor.execute('INSERT INTO Alumnos (Id, Nombre, Apellido) VALUES (5, "Joaquin", "Solano")')
cursor.execute('INSERT INTO Alumnos (Id, Nombre, Apellido) VALUES (6, "Teresa", "Gutierrez")')
cursor.execute('INSERT INTO Alumnos (Id, Nombre, Apellido) VALUES (7, "Antonio", "Perez")')
cursor.execute('INSERT INTO Alumnos (Id, Nombre, Apellido) VALUES (8, "Paola", "Jara")')

query = 'SELECT * FROM Alumnos WHERE Nombre = "Maria"'
rows = cursor.execute(query)
data = rows.fetchall()
print(data)

cursor.close()
# cerrar coneccion
conn.close()