''''
clase base auto con un metodo arrancar() y atributos marca modelo y velocidad maxima
subclases sedan deportivo y suv
cada uan sobrescribiendo el metodo arrancar()
sub con metodo adicional para activar la traccion 4x4
la clase base debe establecer y obtener la velocidad maxima mediante metodos get y set
asegurando que no supere un limite de 220kmh
crea una lista de vehiculos y utiliza un ciclo 
para mostrar la informacion de cada uno activando sus metodos
'''

class Auto:
    def __init__(self,marca,modelo,velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.__velocidad_maxima = velocidad_maxima

    def arrancar(self):
        pass

    def get_velocidad_maxima(self):
        return self.__velocidad_maxima
    
    def set_velocidad_maxima(self, valor):
        if valor <= 220:
            self.__velocidad_maxima = valor
        else:
            self.__velocidad_maxima = 220

    def __str__(self):
        return f"{self.marca} {self.modelo} - Max: {self.get_velocidad_maxima()} km/h"

class Sedan(Auto):
    def arrancar(self):
        print("El sedan arranca suavemente.")

class Deportivo(Auto):
    def arrancar(self):
        print("El deportivo ruge al arrancar")

class SUV(Auto):
    def arrancar(self):
        print("La SUV enciende su potente motor.")

    def activar_traccion_4x4(self):
        print("La traccion 4x4 ha sido activada")

vehiculos = [
    Sedan("Nissan","Versa",150),
    Deportivo("Chevrolet","Camaro",250),
    Sedan("Toyota","Corolla",180),
    Deportivo("Porsche","911",320),
    SUV("Jeep","Wrangler",200),
    SUV("Ford","Explorer",210)
]

for v in vehiculos:
    v.set_velocidad_maxima(v.get_velocidad_maxima())
    print(v)
    v.arrancar()
    if isinstance(v, SUV):
        v.activar_traccion_4x4()
    print()

print("-------------------------------------------\n")