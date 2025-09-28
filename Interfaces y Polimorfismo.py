from abc import ABC, abstractmethod

# Ejercicio 5: Interfaces - Instrumentos musicales

class IInstrumento(ABC):
    @abstractmethod
    def tocar(self):
        # Método que todas las clases deben implementar
        pass
    
    @property
    @abstractmethod
    def nombre(self):
        # Propiedad abstracta para el nombre
        pass

class Guitarra(IInstrumento):
    def __init__(self, nombre):
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    def tocar(self):
        return "  Sonido de guitarra"

class Piano(IInstrumento):
    def __init__(self, nombre):
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    def tocar(self):
        return "  Sonido de piano"

# Prueba del Ejercicio 5

print("=== EJERCICIO 5: INTERFACES Y POLIMORFISMO ===")

# Lista de instrumentos (polimorfismo)
instrumentos = []

# Agregar 4 guitarras
instrumentos.append(Guitarra("Fender Stratocaster"))
instrumentos.append(Guitarra("Gibson Les Paul"))
instrumentos.append(Guitarra("Yamaha Acústica"))
instrumentos.append(Guitarra("Ibanez Eléctrica"))

# Agregar 4 pianos
instrumentos.append(Piano("Yamaha Grand"))
instrumentos.append(Piano("Kawai Digital"))
instrumentos.append(Piano("Steinway Concert"))
instrumentos.append(Piano("Casio Keyboard"))

# Recorrer la lista y tocar instrumentos
print("Concierto de instrumentos:")
for instrumento in instrumentos:
    print(f"{instrumento.nombre}: {instrumento.tocar()}")

print("\n" + "="*50)
print(" ¡Todos los ejercicios completados exitosamente! ")
