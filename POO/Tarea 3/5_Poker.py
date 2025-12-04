'''
Define una clase Carta con atributos palo y valor. 
Crea subclases CartaNumerada y CartaEspecial con atributos específicos. 
Usa polimorfismo para que todas las cartas tengan un método mostrar().
----------------------------------------------------------------
Nombre: Juan Pablo Garcia
Grupo: 213023_24
Programa: Ingenieria de sistemas
'''
import random
class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
    def mostrar(self):
        pass

'''Subclases'''
class CartaNumerada(Carta):
    def mostrar(self):
        print(f"[{self.palo:<9}] 🔹 Soldado raso nivel *\033[1m{self.valor}\033[0m*") # \033[1m{}\033[0m son como etiquetas para la negrita
class CartaEspecial(Carta):
    def mostrar(self):
        print(f"[{self.palo:<9}] 👑 Heroe Legendario: *\033[1m{self.valor}\033[0m* 🔥")

Mazo_Completo = []
Palos = ["Corazones","Diamantes","Treboles","Picas"]

'''Llenando el mazo con las 52 cartas que un mazo de poker estandar tiene'''
for palo in Palos:
    for valor in range (2,11):
        nueva_carta = CartaNumerada(palo, valor)
        Mazo_Completo.append(nueva_carta)
for palo in Palos:
    for valor in ["A","J","Q","K"]:
        nueva_carta = CartaEspecial(palo, valor)
        Mazo_Completo.append(nueva_carta)

'''La funcion sample garantiza que los 5 elementos sean únicos y distintos, tal como si te repartieran las primeras 5 cartas del tope del mazo'''
mano_jugador = random.sample(Mazo_Completo, 5)

'''Ahora mostramos la mano'''
print("\n--------------Tu mano es:--------------")
for carta in mano_jugador:
    carta.mostrar()
print("---------------------------------------\n")
