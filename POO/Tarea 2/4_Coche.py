''' Crea una clase Coche con los atributos marca, modelo, ano, y velocidad. Agrega metodos acelerar() para incrementar la
velocidad en 10 unidades y frenar() para reducir la velocidad en 10 unidades (sin bajar de 0). Crea un objeto Coche, acelera y
frena varias veces, y muestra la velocidad final del coche. 
----------------------------------------------------------------
Nombre: Juan Pablo Garcia Carrillo
Grupo: 213023_24
Programa: Ingenieria de sistemas'''

class Coche:

    def __init__(self, marca, modelo, year, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        if self.velocidad <= 10:
            self.velocidad = 0
        else:
            self.velocidad -= 10

    def velocidad_actual(self):
        if self.velocidad > 50:
            print(f"\nEl {self.marca} {self.modelo} del {self.year} va a {self.velocidad}km/h, excediendo el limite de velocidad!")
        elif self.velocidad == 0:
            print(f"\nEl {self.marca} {self.modelo} del {self.year} se detuvo")
        else:
            print(f"\nEl {self.marca} {self.modelo} del {self.year} va a {self.velocidad}km/h")

''' Instancia '''
coche1 = Coche("Mazda","Milenio",1999,30)

coche1.acelerar() # subimos a 40
coche1.acelerar() # subimos a 50
coche1.acelerar() # subimos a 60
coche1.velocidad_actual()
coche1.frenar() # bajamos a 50
coche1.frenar() # bajamos a 40
coche1.frenar() # bajamos a 30
coche1.velocidad_actual()
coche1.frenar() # bajamos a 20
coche1.frenar() # bajamos a 10
coche1.frenar() # bajamos a 0
coche1.frenar() # aqui testeamos que la velocidad no pase a ser un numero negativo
coche1.velocidad_actual()
print("-" * 30)