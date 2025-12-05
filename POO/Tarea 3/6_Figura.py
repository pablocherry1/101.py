'''
Crea una clase Figura con un atributo __area. 
Luego, crea subclases Rectangulo y Triangulo que tengan métodos para calcular su área 
y permitan obtener el valor de __area de manera controlada mediante encapsulamiento.
----------------------------------------------------------------
Nombre: Juan Pablo Garcia
Grupo: 213023_24
Programa: Ingenieria de sistemas
'''
class Figura:
    def __init__(self):
        self.__area = 0
    '''Defieniendo getter y setter'''    
    def get_area(self):
        return self.__area
    def _set_area(self, value):
        self.__area = value

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    def calc_area(self):
        area = self.base * self.altura
        self._set_area(area)
    def mostrar_area(self):
        print(f"El area del rectangulo es: {self.get_area()}")

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    def calc_area(self):
        area = (self.base * self.altura) / 2
        self._set_area(area)
    def mostrar_area(self):
        print(f"El area del triangulo es: {self.get_area()}")

'''Crear objetos para probar el codigo'''
Figura1 = Rectangulo(25, 10)
Figura1.calc_area()
Figura1.mostrar_area()

Figura2 = Triangulo(18, 4)
Figura2.calc_area()
Figura2.mostrar_area()

Figura3 = Rectangulo(40, 20)
Figura3.calc_area()
Figura3.mostrar_area()