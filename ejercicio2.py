class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        print(f"Estudiantes en la clase {self.nombre}:")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.nombre}")

clase = Clase("Matemáticas")
estudiante1 = Estudiante("josep")
estudiante2 = Estudiante("valeria")

clase.agregar_estudiante(estudiante1)
clase.agregar_estudiante(estudiante2)

clase.listar_estudiantes()
