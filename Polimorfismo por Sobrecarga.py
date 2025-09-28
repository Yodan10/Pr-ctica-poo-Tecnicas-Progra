# Ejercicio 3: Polimorfismo - Reproductor con diferentes tipos de medios

class Reproductor:
    
    def reproducir(self, medio, volumen=None, duracion=None):
        # Un método que maneja diferentes casos de reproducción
        
        if volumen is None and duracion is None:
            # Solo el medio
            print(f" Reproduciendo: {medio}")
        elif duracion is None:
            # Medio y volumen
            print(f" Reproduciendo: {medio} - Volumen: {volumen}%")
        else:
            # Medio, volumen y duración
            print(f" Reproduciendo: {medio} - Volumen: {volumen}% - Duración: {duracion}min")

# Prueba del Ejercicio 3

print("=== EJERCICIO 3: POLIMORFISMO POR SOBRECARGA ===")
player = Reproductor()
player.reproducir("Canción.mp3")     # Solo medio
player.reproducir("Película.mp4", 80)  # Medio y volumen
player.reproducir("Podcast.mp3", 60, 30)  # Los tres parámetros
print()
