'''
Crea una clase Producto con atributos encapsulados __nombre, __precio, y un método aplicar_descuento(porcentaje). 
Crea subclases ProductoDigital y ProductoFisico que sobrescriban el método de descuento para aplicar descuentos diferentes.
----------------------------------------------------------------
Nombre: Juan Pablo Garcia
Grupo: 213023_24
Programa: Ingenieria de sistemas
'''

class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = int(precio)
    '''Defieniendo getters'''    
    def _get_nombre(self):
        return self.__nombre
    def _get_precio(self):
        return self.__precio
    '''Definiendo setters'''
    def _set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    def aplicar_descuento(self, porcentaje):
        pass

'''Subclases'''
class ProductoDigital(Producto):
    def aplicar_descuento(self, porcentaje):
        precio_actual = self._get_precio()
        # El descuento se calcula sobre el precio actual
        porcentaje += 5 #Al ser digital le regalamos un 5% extra de descuento
        monto_descuento = precio_actual * (porcentaje / 100) # (200 * 0.40 = 80)
        nuevo_precio = precio_actual - monto_descuento      # (200 - 80 = 120)
        self._set_precio(nuevo_precio)
        nombre = self._get_nombre()
        print(f"El precio de {nombre} con un descuento del {porcentaje}% (¡5% extra por ser una compra online!) es {nuevo_precio:.2f}")
class ProductoFisico(Producto):
    def aplicar_descuento(self, porcentaje):
        precio_actual = self._get_precio()
        # El descuento se calcula sobre el precio actual
        monto_descuento = precio_actual * (porcentaje / 100) # (200 * 0.40 = 80)
        nuevo_precio = precio_actual - monto_descuento      # (200 - 80 = 120)
        self._set_precio(nuevo_precio)
        nombre = self._get_nombre()
        print(f"El precio de {nombre} con un descuento del {porcentaje}% es {nuevo_precio:.2f}")
      
        
'''Instancias'''
descuento1 = ProductoDigital("Parlante",200)
descuento2 = ProductoFisico("Parlante",200)
descuento3 = ProductoDigital("Lavadora",3500)
descuento4 = ProductoFisico("Lavadora",3500)

'''Aplicar descuento'''
descuento1.aplicar_descuento(30)
descuento2.aplicar_descuento(30)
descuento3.aplicar_descuento(15)
descuento4.aplicar_descuento(15)