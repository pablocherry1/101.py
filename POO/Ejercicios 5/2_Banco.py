'''
Modificar el método retirar en Banco para que verifique que hay
suficiente saldo antes de hacer la retirada.
'''


# Definiendo la clase

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    # Metodo

    def retirar(self, cantidad):
        # Validación de cantidad negativa o cero
        if cantidad <= 0:
            # Devolvemos False y un mensaje de error claro
            return False, "La cantidad a retirar debe ser positiva."
        
        # Verificación de saldo
        elif cantidad > self.saldo:
            # Devolvemos False y un mensaje de saldo insuficiente
            return False, "Saldo insuficiente para realizar el retiro."

        # Retiro exitoso
        else:
            self.saldo -= cantidad
            # Devolvemos True y el nuevo saldo como resultado
            return True, f"Retiro exitoso. Nuevo saldo: {self.saldo}."

# Instancia
juan = CuentaBancaria(500)

# Retiro exitoso
exito, mensaje = juan.retirar(300)
print(f"Resultado 1: {exito} - {mensaje}")

# Intento de retiro negativo
exito, mensaje = juan.retirar(-50)
print(f"Resultado 2: {exito} - {mensaje}")

# Saldo insuficiente
exito, mensaje = juan.retirar(300)
print(f"Resultado 3: {exito} - {mensaje}")