'''
Define una clase Animal con el método hacer_sonido(). 
Crea subclases Leon, Elefante y Serpiente que sobrescriban hacer_sonido() con sonidos distintos. 
Usa una lista de animales y polimorfismo para hacer que todos emitan sus sonidos.
----------------------------------------------------------------
Nombre: Juan Pablo Garcia
Grupo: 213023_24
Programa: Ingenieria de sistemas
'''
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    def hacer_sonido():
        pass

'''Subclases'''
class Leon(Animal):
    def hacer_sonido(self):
        print(f"El majestuoso leon {self.nombre} con ferocidad indomable ruge \n¡GRRRRRRRRRR!")
class Elefante(Animal):
    def hacer_sonido(self):
        print(f"El colosal elefante {self.nombre} con fuerza estrepitosa barita con su trompa \n¡FUUUUUUU!")
class Serpiente(Animal):
    def hacer_sonido(self):
        print(f"La sigilosa serpiente {self.nombre} con amenaza letal sisea \n¡Sssss Sssss!")
class Lobo(Animal):
    def hacer_sonido(self):
        print(f"El solitario lobo {self.nombre} clamando a la luna aúlla \n¡AUUUUUUUU!")
class Caballo(Animal):
    def hacer_sonido(self):
        print(f"El indomable caballo {self.nombre} desafiando al viento relincha \n¡IIIIHHHHHHHH!")

# Probando el código
jaula = [
    Leon("Mufasa"),
    Elefante("Dumbo"),
    Serpiente("Nagini"),
    Lobo("Fenrir"),
    Caballo("Bucefalo")
]

for animal in jaula:
    print("---------------------------------------------------------------------------------")
    animal.hacer_sonido()
