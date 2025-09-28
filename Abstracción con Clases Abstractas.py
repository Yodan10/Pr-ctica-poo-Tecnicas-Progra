from abc import ABC, abstractmethod

# Ejercicio 4: Abstracción - Vehículos con diferentes métodos de movimiento

class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        # Método abstracto - debe implementarse en clases hijas
        pass

class Coche(Vehiculo):
    def __init__(self, modelo, velocidad):
        self.modelo = modelo
        self.velocidad = velocidad
    
    def mover(self):
        # Implementación para coche
        print(f" Coche {self.modelo} circula a {self.velocidad} km/h")

class Avion(Vehiculo):
    def __init__(self, modelo, altitud):
        self.modelo = modelo
        self.altitud = altitud
    
    def mover(self):
        # Implementación para avión
        print(f" Avión {self.modelo} vuela a {self.altitud} metros")

# Prueba del Ejercicio 4

print("=== EJERCICIO 4: ABSTRACCIÓN CON CLASES ABSTRACTAS ===")
coche1 = Coche("Toyota", 120)
avion1 = Avion("Boeing 747", 10000)

coche1.mover()
avion1.mover()
print()
