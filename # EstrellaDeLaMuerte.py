# EstrellaDeLaMuerte.py

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_vida = 1000

    def destruir_nave_aliada(self, nave_aliada):
        if nave_aliada.vida <= self.puntos_vida:
            print(f"La Estrella de la Muerte ha destruido la nave aliada {nave_aliada.nombre}.")
            self.puntos_vida -= nave_aliada.vida
        else:
            print(f"No se puede destruir la nave aliada {nave_aliada.nombre}. La vida es demasiado alta.")

# Naves.py
from EstrellaDeLaMuerte import EstrellaDeLaMuerte

class NaveAliada(EstrellaDeLaMuerte):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

class NavePequena(NaveAliada):
    def __init__(self, nombre, vida):
        super().__init__(nombre, vida)

class NaveGrande(NaveAliada):
    def __init__(self, nombre, vida):
        super().__init__(nombre, vida)

# main.py
from EstrellaDeLaMuerte import EstrellaDeLaMuerte
from Naves import NavePequena, NaveGrande

# Crear instancias de la Estrella de la Muerte y naves aliadas
estrella_muerte = EstrellaDeLaMuerte()
nave_pequena = NavePequena("Nave Pequeña", 200)
nave_grande = NaveGrande("Nave Grande", 600)

# Llamar al método destruir_nave_aliada para cada nave aliada
estrella_muerte.destruir_nave_aliada(nave_pequena)
estrella_muerte.destruir_nave_aliada(nave_grande)
