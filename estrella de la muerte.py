# Planetas.py

from enum import Enum

class Clasificacion(Enum):
    CONCORDIA = 1
    ILUM = 2
    KAMINO = 3

class Planeta:
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion.value

class Concordia(Planeta):
    def __init__(self):
        super().__init__("Concordia", 500, Clasificacion.CONCORDIA)

class Ilum(Planeta):
    def __init__(self):
        super().__init__("Ilum", 1200, Clasificacion.ILUM)

class Kamino(Planeta):
    def __init__(self):
        super().__init__("Kamino", 800, Clasificacion.KAMINO)

concordia_planeta = Concordia()
ilum_planeta = Ilum()
kamino_planeta = Kamino()

print(f"Nombre: {concordia_planeta.nombre}, Volumen: {concordia_planeta.volumen} km³, Clasificación: {concordia_planeta.clasificacion}")
print(f"Nombre: {ilum_planeta.nombre}, Volumen: {ilum_planeta.volumen} km³, Clasificación: {ilum_planeta.clasificacion}")
print(f"Nombre: {kamino_planeta.nombre}, Volumen: {kamino_planeta.volumen} km³, Clasificación: {kamino_planeta.clasificacion}")


# EstrellaDeLaMuerte.py


class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_vida = 1000

    def destruir_planeta(self, planeta):
        if planeta.volumen <= self.puntos_vida:
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.puntos_vida -= planeta.volumen
        else:
            print(f"No se puede destruir el planeta {planeta.nombre}. El volumen es mayor.")


estrella_muerte = EstrellaDeLaMuerte()
concordia_planeta = Concordia()
ilum_planeta = Ilum()
kamino_planeta = Kamino()

estrella_muerte.destruir_planeta(concordia_planeta)
estrella_muerte.destruir_planeta(ilum_planeta)
estrella_muerte.destruir_planeta(kamino_planeta)



