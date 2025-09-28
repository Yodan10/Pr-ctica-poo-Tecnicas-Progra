# Ejercicio 2: Herencia - Estudiantes con diferentes carreras
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, Edad: {self.edad} años")

class Ingenieria(Estudiante):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)  # Hereda de Estudiante
        self.especialidad = especialidad
    
    def mostrar_info(self):
        # Sobrescribe con información de ingeniería
        print(f"Ingeniería: {self.nombre}, Edad: {self.edad}, Especialidad: {self.especialidad}")

class Medicina(Estudiante):
    def __init__(self, nombre, edad, semestre):
        super().__init__(nombre, edad)  # Hereda de Estudiante
        self.semestre = semestre
    
    def mostrar_info(self):
        # Sobrescribe con información de medicina
        print(f"Medicina: {self.nombre}, Edad: {self.edad}, Semestre: {self.semestre}")

# Prueba del Ejercicio 2

print("=== EJERCICIO 2: HERENCIA Y SOBRESCRITURA ===")
estudiante1 = Estudiante("María", 20)
ingeniero1 = Ingenieria("Carlos", 22, "Sistemas")
medico1 = Medicina("Ana", 23, 8)

estudiante1.mostrar_info()
ingeniero1.mostrar_info()
medico1.mostrar_info()
print()
