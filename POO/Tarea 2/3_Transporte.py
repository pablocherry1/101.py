'''Crear una clase abstracta Transporte con el método abstracto moverse. 
Crear clases Coche y Bicicleta que implementen este método. 
----------------------------------------------------------------
Nombre: Juan Pablo Garcia Carrillo
Grupo: 213023_24
Programa: Ingenieria de sistemas'''

from abc import ABC, abstractmethod

''' 1. Clase Abstracta para todos los tipos de transporte. '''
class Transporte(ABC):
    
    def __init__(self, color: str, posicion_inicial: int):
        self.color = color
        self.posicion = posicion_inicial 
        # Se establece la posición inicial en el constructor de la base

    ''' 2. Método Abstracto '''
    @abstractmethod
    def moverse(self, distancia: int):
        pass # Se deja vacío o con 'pass' porque la implementación la hacen las clases hijas.
    
    def estado_actual(self): #Muestra el estado actual del vehículo.
        return f"El vehículo {self.color} está en la posición {self.posicion}."
    

''' 3. Implementación de Coche '''
class Coche(Transporte):
    def __init__(self, color, posicion_inicial):
        super().__init__(color, posicion_inicial)
        
    def moverse(self, distancia):
        if distancia < 0:
            self.posicion += distancia
            print(f"El coche retrocedió y ahora está en {self.posicion} metros.")
        elif distancia > 0:
            self.posicion += distancia
            print(f"El coche avanzó hasta los {self.posicion} metros de la salida.")
        else:
             print("El coche está detenido.")
        
''' 4. Implementación de Bicicleta '''
class Bicicleta(Transporte):
    def __init__(self, color, posicion_inicial):
        super().__init__(color, posicion_inicial)
    
    def moverse(self, distancia):
        if distancia > 100:
            print("¡Eso es demasiado para una bicicleta! Solo avanza 100m.")
            distancia = 100
            
        if distancia > 0:
            self.posicion += distancia
            print(f"La bicicleta pedaleó hasta los {self.posicion} metros.")
        else:
             print("La bicicleta se detuvo o no puede retroceder tanto.")

''' 5. Instancias '''
coche = Coche("Rojo", 0)
bicicleta = Bicicleta("Verde", 50)

print("--- Movimientos ---")
coche.moverse(50)
bicicleta.moverse(60)
coche.moverse(-10)

print("--- Estados Finales ---")
print(coche.estado_actual())
print(bicicleta.estado_actual())