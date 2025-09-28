# Ejercicio 1: Encapsulamiento - Proteger el saldo de la cuenta

class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0  # Atributo privado (encapsulado)
    
    def depositar(self, cantidad):
        # Solo deposita si la cantidad es positiva
        if cantidad > 0:
            self.__saldo += cantidad
            print(f" Depositado: ${cantidad}")
        else:
            print(" Error: La cantidad debe ser mayor a cero")
    
    def retirar(self, cantidad):
        # Solo retira si hay suficiente saldo
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f" Retirado: ${cantidad}")
        else:
            print(" Error: Saldo insuficiente")
    
    def obtener_saldo(self):
        # Método para ver el saldo
        return self.__saldo

# Prueba del Ejercicio 1

print("=== EJERCICIO 1: ENCAPSULAMIENTO ===")
mi_cuenta = CuentaBancaria()
mi_cuenta.depositar(1000)
mi_cuenta.retirar(300)
mi_cuenta.retirar(800)  # Esto fallará
print(f"Saldo final: ${mi_cuenta.obtener_saldo()}")
print()
