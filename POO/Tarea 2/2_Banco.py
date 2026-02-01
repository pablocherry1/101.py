'''
Modificar el método retirar en Banco para que verifique que hay
suficiente saldo antes de hacer la retirada.
----------------------------------------------------------------
Nombre: Juan Pablo Garcia Carrillo
Grupo: 213023_24
Programa: Ingenieria de sistemas
'''

# Definiendo la clase
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    # Metodo
    def retirar(self, cantidad):
        # Validación de cantidad negativa o cero
        if cantidad <= 0:
            return False, "La cantidad a retirar debe ser positiva." # Devolvemos False y un mensaje de error claro
        
        # Verificación de saldo
        elif cantidad > self.saldo:  
            return False, "Saldo insuficiente para realizar el retiro." # Devolvemos False y un mensaje de saldo insuficiente

        # Retiro exitoso
        else:
            self.saldo -= cantidad
            return True, f"Retiro exitoso. Nuevo saldo: {self.saldo}." # Devolvemos True y el nuevo saldo como resultado

# Instancia
juan = CuentaBancaria(500)

exito, mensaje = juan.retirar(300) # Retiro exitoso
print(f"Resultado 1: {exito} - {mensaje}")

exito, mensaje = juan.retirar(-50) # Intento de retiro negativo
print(f"Resultado 2: {exito} - {mensaje}")

exito, mensaje = juan.retirar(300) # Saldo insuficiente
print(f"Resultado 3: {exito} - {mensaje}")