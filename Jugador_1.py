class Jugador1:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
    
    def mostrarDatos(self):
        return'El nombre del luchador es {} con un poder de {}%'.format(self.nombre, self.poder)
        
luchador = Jugador1('Goku', 100)
print(luchador.mostrarDatos())