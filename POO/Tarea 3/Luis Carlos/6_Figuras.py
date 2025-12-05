class Figura:
    def __init__(self):
        # Inicializamos el area en 0 o None. 
        # Es privado (__), solo accesible dentro de esta clase.
        self.__area = 0
    
    # Getter: Permite OBTENER el valor de forma pública
    def get_area(self):
        return self.__area

    # Setter protegido: Permite a las subclases o a la propia clase MODIFICAR el valor.
    # Usamos un guion bajo simple (_) por convención para indicar que es para uso interno/herencia.
    def _set_area(self, valor):
            self.__area = valor

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__() # Inicializa la parte de Figura
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Fórmula: base * altura
        resultado = self.base * self.altura
        # Usamos el setter de la clase padre para guardar el valor en __area
        self._set_area(resultado)

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Fórmula: (base * altura) / 2
        resultado = (self.base * self.altura) / 2
        self._set_area(resultado)

# --- Bloque de Prueba ---

# 1. Crear un Rectángulo
mi_rectangulo = Rectangulo(10, 5)
mi_rectangulo.calcular_area()
print(f"Área del Rectángulo: {mi_rectangulo.get_area()}")

# 2. Crear un Triángulo
mi_triangulo = Triangulo(10, 5)
mi_triangulo.calcular_area()
print(f"Área del Triángulo: {mi_triangulo.get_area()}")