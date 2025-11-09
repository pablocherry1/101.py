''' Clase Restaurante con Menú y Órdenes: 
Crea una clase Restaurante que tenga un atributo menu (una lista de platos disponibles, cada uno como un diccionario con nombre, precio y tiempo_preparacion). 
Añade métodos agregar_plato(plato) para agregar un plato al menú,ver_menu() que muestre el menú completo, y realizar_orden(lista_platos) 
que calcule el costo total y el tiempo de preparación estimado para una lista de platos ordenados. 
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

    def mostrar_menu(self): #Iteracion sobre la lista menu
        print(f"\n--- Menu de {self.nombre} ---")
        for i, plato in enumerate(self.menu):
            print(f"{i+1}. {plato['nombre']:<21} | Precio: ${plato['precio']:<8} | Tiempo: {plato['tiempo_preparacion']} min.")
        print("---------------------------------")

    def realizar_orden(self, lista_indices_platos):
        """Calcula el costo total y el tiempo de preparacion estimado 
        para una orden dada como una lista ej: [1,2,5] """
        costo_total = 0
        tiempo_estimado = 0
        platos_ordenados = []

        print(f"\n--- Procesando Orden: {lista_indices_platos} ---")
        
        for i in lista_indices_platos:
            # 1. Ajustar el indice: de base 1 (lo que ve el usuario) 
            # a base 0 (lo que usa Python)
            indice_base_0 = i - 1 

            plato = self.menu[indice_base_0]
            
            # 2. Sumar costos y tiempos
            costo_total += plato['precio']
            tiempo_estimado += plato['tiempo_preparacion'] 
            platos_ordenados.append(plato['nombre'])

        
        # 3. Mostrar el resumen
        print("--- Resumen de la Orden ---")
        # Bucle para imprimir cada plato con un guion
        for plato in platos_ordenados:
             print(f"  - {plato}")
        print(f"Costo Total: **${costo_total}**")
        print(f"Tiempo de Preparación Estimado (Suma): **{tiempo_estimado} minutos**")

# 1. Crear el restaurante
mi_restaurante = Restaurante("The Bear")

# 2. Agregar platos
mi_restaurante.agregar_plato("Focaccia", 12, 20)
mi_restaurante.agregar_plato("Welcome Broth", 10, 15)
mi_restaurante.agregar_plato("Bucatini", 30, 20)
mi_restaurante.agregar_plato("Seven Fishes", 70, 45)
mi_restaurante.agregar_plato("The T-Bone", 60, 30)
mi_restaurante.agregar_plato("The Bear Honey Bun", 10, 11)
mi_restaurante.agregar_plato("\"The Michael\" Cannoli", 10, 15)
mi_restaurante.agregar_plato("Sydney\'s Donut", 15, 10)

# 3. Mostrar el menu
mi_restaurante.mostrar_menu()

# 4. Realizar orden
mi_restaurante.realizar_orden([1, 3, 6])

# Simulacion de Orden 2
mi_restaurante.realizar_orden([2, 4, 5, 8])