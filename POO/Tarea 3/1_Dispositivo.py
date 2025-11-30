'''
Crea una clase Dispositivo con un método enviar_mensaje(mensaje). 
Luego, crea subclases Telefono, Tablet y Computadora, cada una con su propia implementación de enviar_mensaje(). 
Usa polimorfismo para simular una lista de dispositivos enviando mensajes.
----------------------------------------------------------------
Nombre: Juan Pablo Garcia Carrillo
Grupo: 213023_24
Programa: Ingenieria de sistemas
'''

class Dispositivo:
    def __init__(self, sistema_operativo):
        self.sistema_operativo = sistema_operativo
    
    def enviar_mensaje(self, mensaje):
        pass

class Telefono(Dispositivo):
    def enviar_mensaje(self, mensaje):
        print(f"Mensaje enviado por SMS desde un celular {self.sistema_operativo}: \n{mensaje}")

class Tablet(Dispositivo):
    def enviar_mensaje(self, mensaje):
        print(f"Mensaje enviado por wifi desde una Tablet con {self.sistema_operativo}: \n{mensaje}")

class Computadora(Dispositivo):
    def enviar_mensaje(self, mensaje):
        print(f"Mensaje enviado a traves de un servidor con una computadora corriendo {self.sistema_operativo}: \n{mensaje}")

dispositivos = [
    Telefono("Android"),
    Tablet("iPadOS"),
    Computadora("Debian"),
    Computadora("MacOS"),
    Computadora ("Ubuntu")
]

for d in dispositivos:
    print("\n--- Nuevo Envío ---")
    d.enviar_mensaje("**Hello it's me**")