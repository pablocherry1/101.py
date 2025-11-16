''' Crear una clase Universidad con un atributo de clase num_estudiantes. 
Cada vez que se cree un estudiante, incrementar el atributo num_estudiantes. 
----------------------------------------------------------------
Nombre: Juan Pablo Garcia Carrillo
Grupo: 213023_24
Programa: Ingenieria de sistemas'''

class Universidad:
    num_estudiantes = 0 
 
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
         
        Universidad.num_estudiantes += 1

universidad1 = Universidad("UNAD") 
print(f"Estudiantes iniciales: {Universidad.num_estudiantes}")

estudiante1 = Estudiante("Juan", "Ingeniería de Sistemas")
print(f"Estudiantes en total: {Universidad.num_estudiantes}")

estudiante2 = Estudiante("Paola", "Administracion de empresas")

estudiante2 = Estudiante("Carolina", "Ingenieria ambiental")

print(f"La {universidad1.nombre} tiene {universidad1.num_estudiantes} estudiantes en estos momentos")