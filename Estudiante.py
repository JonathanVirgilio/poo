class Estudiantes:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def registroestudiantes(self):
        return 'El nombre del estudiante es : {} su carrera es: {}'.format(self.nombre,self.carrera)

DatosEstudiantes= Estudiantes ("Braulio", "ingeniera en desarrollo de sofware")
print(DatosEstudiantes.registroestudiantes())