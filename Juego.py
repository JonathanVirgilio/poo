from Jugador_1 import Jugador1
from Jugador2 import Jugador2
from Jugador_1 import luchador
from Jugador2 import luchador2
class Juego(Jugador1,Jugador2):
    pass
    def luchadorEs():
        return'Luchador {} su poder es {} vs Luchador {} su poder es {}'.format(luchador.nombre, luchador.poder, luchador2.nombre2, luchador2.poder2)

luchadores1 = Juego
print(luchadores1.luchadorEs())
print("El luchador " + luchador.nombre + " lanza un ataque")
print("El luchador " + luchador2.nombre2 + " recibe un ataque")
print("El poder del luchador" + luchador2.nombre2 + " es de 70%")