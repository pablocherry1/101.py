import random

class Generador:
    def __init__(self, longitud):
        self.longitud = longitud
        self.caracteres = ""
        self.contrasena = ""

    def generar(self):
        """Metodo que sera sobrescrito"""
        pass

class GeneradorSeguro(Generador):
    def __init__(self, longitud):
        # Lllamamos al constructor de la clase padre
        super().__init__(longitud)

        # Definimos los atributos con los pools de caracteres
        self.minusculas = "abcdefghijklmnopqrstuvwxyz"
        self.mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numeros = "0123456789"
        self.especiales = "¿¡?=)(/¨*+-%&$#!."

        # Unimos todo para tener un pool general
        self.todos_los_caracteres = self.minusculas + self.mayusculas + self.numeros + self.especiales

        # Validamos de inmediato al crear el objeto
        self.validar_longitud()

    def validar_longitud(self):
        if self.longitud < 8:
            # 
            print("Error: La longitud debe ser de minimo 8 caracteres")
            return False
        
        # Para que no repita datos
        if self.longitud > len(self.todos_los_caracteres):
            print(f"Error: no hay tantos caracteres unicos disponibles (Maximo {len(self.todos_los_caracteres)}).")
            return False
        
        return True