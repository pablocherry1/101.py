'''
Nombre: Juan Pablo Garcia
Grupo: 213023_24
Programa: Ingenieria de sistemas
'''

import random

class Generador: # Este es un generador de contraseñas basicas
    def __init__(self, longitud):
        self.longitud = longitud
        self.minusculas = "abcdefghijklmnopqrstuvwxyz"
        self.contrasena = ""

    def validar_longitud(self):
        
        if self.longitud > len(self.minusculas):
            print(f"Error: el abecedario solo tiene {len(self.minusculas)} letras.")
            return False
        
        return True

    def generar(self): 
        password = random.sample(self.minusculas, self.longitud)
        # Para convertir la contraseña de una lista a un string
        self.contrasena = "".join(password)
        return self.contrasena

class GeneradorSeguro(Generador):
    def __init__(self, longitud):

        # Lllamamos al constructor de la clase padre
        super().__init__(longitud)
        
        # Definimos los atributos con los pools de caracteres restantes
        self.mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numeros = "0123456789"
        self.especiales = "¿¡?=)(/¨*+-%&$#!."

        # Unimos todo para tener un pool general
        self.todos_los_caracteres = self.minusculas + self.mayusculas + self.numeros + self.especiales
        
    def validar_longitud(self):
        
        if self.longitud > len(self.todos_los_caracteres):
            print(f"Error: Maximo {len(self.todos_los_caracteres)} caracteres unicos.")
            return False
        
        return True
    
    def generar(self):
        obligatorios = [
            random.choice(self.minusculas),
            random.choice(self.mayusculas),
            random.choice(self.numeros),
            random.choice(self.especiales)
        ]

        #Utilizamos set para hacer una resta entre conjuntos
        pool_limpio = list(set(self.todos_los_caracteres) - set(obligatorios))
        faltantes = self.longitud - len(obligatorios)
        resto = random.sample(pool_limpio, faltantes)
        password = resto + obligatorios
        random.shuffle(password)
        self.contrasena = "".join(password)

        return self.contrasena
    
while True:
    entrada = input("\nIntroduce la logitud (minimo 8) o escribe 'salir' para terminar: ").lower()

    if entrada == 'salir':
        print("Gracias por usar el generador! Feliz dia.")
        break

    try:
        longitud = int(entrada)

        if longitud < 8:
            print("Error: La longitud debe ser de minimo 8 caracteres")
            continue

        print("\nQue tipo de contraseña prefieres?")
        print("1. Basica (solo minusculas)")
        print("2. Segura (Incluye tambien mayusculas, numeros, y caracteres especiales)")
        opcion = input("Elige una opcion (1 o 2): ")

        if opcion == "1":
            mi_generador = Generador(longitud)
        elif opcion == "2":
            mi_generador = GeneradorSeguro(longitud)
        else:
            print("Opcion no valida.")
            continue #Regresa al inicio del while

        if mi_generador.validar_longitud():
            password_final = mi_generador.generar()
            print(f"\nTu contraaseña generada es *-  {password_final}  -*")
            print(f"\nVerificacion: {len(password_final)} caracteres generados.")

    except ValueError:
        print("Error: Ingresa un numero valido o 'salir'.")