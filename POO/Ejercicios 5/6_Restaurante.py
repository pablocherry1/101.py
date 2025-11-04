''' Clase Restaurante con Menú y Órdenes: 
Crea una clase Restaurante que tenga un atributo menu (una lista de platos disponibles, 
cada uno como un diccionario con nombre, precio y tiempo_preparacion). 
Añade métodos agregar_plato(plato) para agregar un plato al menú, 
ver_menu() que muestre el menú completo, y realizar_orden(lista_platos) que calcule el costo total
y el tiempo de preparación estimado para una lista de platos ordenados. 
Prueba esta clase simulando varias órdenes y mostrando los resultados. '''

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = [] # Lista de diccionarios

    def agregar_plato(self, nombre, precio, tiempo_preparacion):
        # Creando el diccionario del plato
        plato_nuevo = {
            "nombre": nombre,
            "precio": precio,
            "tiempo_preparacion": tiempo_preparacion # en minutos
        }
        self.menu.append(plato_nuevo)
        print(f"Plato '{nombre}' añadido al menu de {self.nombre}.")

    def mostrar_menu(self):
        if not self.menu:
            print(f"El menu de {self.nombre} esta vacio!")
            return

        print(f"\n--- Menú de {self.nombre} ---")
        for i, plato in enumerate(self.menu):
            print(f"{i+1}. {plato['nombre']:<20} | Precio: ${plato['precio']:<8.2f} | Tiempo: {plato['tiempo_preparacion']} min.")
        print("---------------------------------")

# 1. Crear el restaurante
mi_restaurante = Restaurante("La Cuchara de Python")

# 2. Agregar platos
mi_restaurante.agregar_plato("Pasta Carbonara", 12.50, 20)
mi_restaurante.agregar_plato("Sopa de Tortuga", 8.00, 15)
mi_restaurante.agregar_plato("Filete 'Big O'", 25.99, 30)

# 3. Mostrar el menú
mi_restaurante.mostrar_menu()