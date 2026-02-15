import os

print("\n-- Simulador Matricula 2026 --")
print("Estudiante: Juan Pablo Garcia")

def contrasena():
    intentos = 3
    while intentos != 0:
        pwd = input("Ingrese la contraseña de acceso:  ")
        intentos -= 1
        if pwd == "2046":
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorrecta!")
    if intentos == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Si el sistema operativo 'nt' windows usa cls, de lo contrario usa clear que sirve para mac y linux

def datos_estudiante():
    """Función para recolectar los datos del estudiante desde la consola."""
    nombre = input("Ingrese su nombre completo: ")
    id_est = input("Ingrese su numero de identificacion: ")
    while True:
        try:
            creditos = int(input("Ingrese la cantidad de creditos a matricular (mínimo 9, máximo 21): "))
            if 9 <= creditos <= 21:
                break  # Si el valor es válido, salimos del bucle.
            else:
                print("Error: La cantidad de créditos debe estar entre 9 y 21. Inténtelo de nuevo.")
        except ValueError:
            print("Error: Debe ingresar un número entero. Inténtelo de nuevo.")
    estrato = int(input("Ingrese su estrato socioeconomico: "))
    genero = input("Ingrese su genero: ")
    respuesta_electoral = input("Posee usted certificado electoral? (S/N):")
    electoral = respuesta_electoral.upper() == "S"
    return id_est, nombre, creditos, estrato, genero, electoral

class Estudiante:
    """Clase que representa a un estudiante y calcula los costos de su matrícula."""
    def __init__(self, id_est, nombre, creditos, estrato, genero, electoral):
        self.id = id_est
        self.nombre = nombre
        self.creditos = creditos
        self.estrato = estrato
        self.genero = genero
        self.electoral = electoral

    def valor_bruto(self):
        credito = 159000
        total = credito * self.creditos
        return total
    
    def descuento_electoral(self):
        return 0.10 if self.electoral else 0
    
    def descuento_estrato(self):
        descuentos = {
            1: 0.15, 2: 0.15,
            3: 0.10, 4: 0.10,
            5: 0.05, 6: 0.05
        }
        # .get() devuelve el valor para el estrato, o 0.0 si no está en el diccionario
        return descuentos.get(self.estrato, 0.0)

    def descuento_total(self):
        return self.descuento_electoral() + self.descuento_estrato()

    def calcular_valor_neto(self):
        """Calcula el valor final a pagar aplicando todos los descuentos."""
        valor_bruto = self.valor_bruto()
        porcentaje_descuento = self.descuento_total()
        valor_descuento = valor_bruto * porcentaje_descuento
        valor_neto = valor_bruto - valor_descuento
        return valor_neto, valor_descuento

contrasena()

# 1. Recolectar los datos
id_est, nombre, creditos, estrato, genero, electoral = datos_estudiante()

# 2. Crear una INSTANCIA de Estudiante con esos datos
instancia_estudiante = Estudiante(id_est, nombre, creditos, estrato, genero, electoral)

# 3. Llamar a los métodos SOBRE LA INSTANCIA
valor_neto, valor_descuento = instancia_estudiante.calcular_valor_neto()

# --- Impresión del Resumen Final ---

# Cortamos el nombre completo en el primer espacio para obtener solo el primer nombre
primer_nombre = instancia_estudiante.nombre.split(' ')[0]

print(f"\n--- Resumen de Matrícula para {primer_nombre} ---")
print(f"Identificación: {instancia_estudiante.id}")
print(f"Nombre completo: {instancia_estudiante.nombre}")
print(f"Créditos matriculados: {instancia_estudiante.creditos}")
print(f"Estrato: {instancia_estudiante.estrato}")
print(f"Certificado electoral: {'Sí' if instancia_estudiante.electoral else 'No'}")
print("\n--- Valores de Matrícula ---")
print(f"Valor bruto de su matricula: ${instancia_estudiante.valor_bruto():,.0f}")
print(f"Valor total del descuento: ${valor_descuento:,.0f}")
print(f"Valor neto de su matricula: ${valor_neto:,.0f}")