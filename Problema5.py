class Alumno:
    def __init__(self, nombre, numero_registro):
        # Inicializar los atributos nombre y número de registro
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    # Método para mostrar la información del estudiante
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print(f"Notas: {self.notas}")

    # Método para asignar la edad del estudiante
    def setAge(self, edad):
        self.edad = edad

    # Método para asignar las notas del estudiante
    def setNota(self, notas):
        self.notas = notas


# Crear un objeto de tipo Alumno
estudiante = Alumno("Andre", "202301")

# Asignar la edad
estudiante.setAge(20)

# Asignar las notas
estudiante.setNota([18, 17, 19])

# Mostrar la información del estudiante
estudiante.display()
