'''
Crear una clase llamada Coche con atributos marca y modelo, y
un método que imprima la marca y el modelo del coche.
----------------------------------------------------------------
Nombre: Juan Pablo Garcia Carrillo
Grupo: 213023_24
Programa: Ingenieria de sistemas
'''

# Definiendo la clase

class Coche:
    def __init__(self,marca,modelo,year,color):
        self.marca = marca
        self.modelo = modelo
        self.year = year # uso year para no escribir ano
        self.color = color

    # Metodo
    def imprimir (self):
        print(f"Un {self.marca} {self.modelo} del año {self.year} color {self.color}")

# Instancias

print("Esta es la lista de coches disponibles:")

coche1 = Coche("Mazda","626",1999,"azul")
coche1.imprimir()

coche2 = Coche("Nissan","Tiida",2008,"rojo")
coche2.imprimir()

coche3 = Coche("Mazda","3",2020,"gris")
coche3.imprimir()

