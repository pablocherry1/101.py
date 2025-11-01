'''
Crear una clase llamada Coche con atributos marca y modelo, y
un método que imprima la marca y el modelo del coche.
'''

# Definiendo la clase

class Coche:
    def __init__(self,marca,modelo,year):
        self.marca = marca
        self.modelo = modelo
        self.year = year

    # Metodo
    def imprimir (self):
        print(f"Un {self.marca} {self.modelo} del año {self.year}")

# Instancias

print("Esta es la lista de coches disponibles:")

coche1 = Coche("Mazda","626",1999)
coche1.imprimir()

coche2 = Coche("Nissan","Tiida",2008)
coche2.imprimir()

coche3 = Coche("Mazda","3",2020)
coche3.imprimir()