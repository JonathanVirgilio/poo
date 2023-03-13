from Estudiante import Estudiantes
from Materias import Materias
from Estudiante import DatosEstudiantes
from Materias import mate
class Notas(Estudiantes, Materias):
    def __init__(self, lab, par):
        self.lab = lab
        self.par = par
    
    def notas(self):
        return'Estudiante {} sus notas en la materia de {} son: Laboratorio: {}. Parcial {}'.format(DatosEstudiantes.nombre, mate.materia, self.lab, self.par)

datos = Notas(5, 9.8)
print(datos.notas())
