from Categorias import Categorias
from Categorias import categorias
class Peliculas(Categorias):
    def __init__(self, dato, dato2, dato3, dato4):
        self.dato = dato
        self.dato2 = dato2
        self.dato3 = dato3
        self.dato4 = dato4

    def nomPeliculas(self):
        cat1 = categorias.cate1
        cat2 = categorias.cate2
        cat3 = categorias.cate3
        if cat1 == self.dato:
            print("Pelicula de accion: " + objeto.dato2)
        else:
            if cat2 == self.dato:
                print("Pelicula de comedia: " + objeto.dato3)
            else:
                if cat3 == self.dato:
                    print("Pelicula de terror: " + objeto.dato4)
                else:
                    print("Error")
        

objeto = Peliculas("Accion", "Rapido y Furiosos", "Son como niños", "Hit, el payaso")
print(objeto.nomPeliculas())