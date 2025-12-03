'''
Define una clase Juguete con métodos encender() y apagar().
Crea subclases Robot y Drone, cada una con un método adicional específico (caminar() en Robot y volar() en Drone). 
Usa encapsulamiento para proteger el estado de encendido y apagado.
----------------------------------------------------------------
Nombre: Juan Pablo Garcia
Grupo: 213023_24
Programa: Ingenieria de sistemas
'''

class Juguete:
    def __init__(self, nombre):
        self.__encendido = False #Variable protegida
        self.nombre = nombre
    def encender(self):
        if not self.__encendido:
            self.__encendido = True
            print(f"{self.nombre} se ha encendido.")
        else:
            print(f"{self.nombre} ya esta encendido.")
    def apagar(self):
        if self.__encendido:
            self.__encendido = False
            print(f"{self.nombre} se ha apagado.")
        else:
            print(f"{self.nombre} ya esta apagado.")
    def consultar_status(self):
        """Metodo para acceder de forma controlada al estado de encendido."""
        estado = "Encendido" if self.__encendido else "Apagado"
        return f"{self.nombre} está: {estado}"

'''Subclases'''
class Robot(Juguete):
    def __init__(self, nombre):
        super().__init__(nombre)
    def caminar(self):
        if self._Juguete__encendido:
            print(f"{self.nombre} esta caminando.")
        else:
            print(f"{self.nombre} no puede caminar, primero debe encenderse.")

class Drone(Juguete):
    def __init__(self, nombre):
        super().__init__(nombre)
    def volar(self):
        if self._Juguete__encendido:
            print(f"{self.nombre} esta volando.")
        else:
            print(f"{self.nombre} no puede volar, primero debe encenderse.")

'''Instancias'''
robot1 = Robot("R2D2")
dron1 = Drone("Halcon Milenario")

print("-Estado Inicial-")
print(robot1.consultar_status())
print(dron1.consultar_status())

print("\n-Pruebas de accion sin cambiar el estado-")
robot1.caminar()
dron1.volar()

print("\n-Encender Juguetes-")
robot1.encender()
dron1.encender()

print("\n-Pruebas de accion despues de encender-")
robot1.caminar()
dron1.volar()


