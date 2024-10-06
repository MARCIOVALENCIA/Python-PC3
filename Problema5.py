class Alumno:
    def __init__(self, nombre, numero_registro):
        
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print(f"Notas: {self.notas}")

    
    def setAge(self, edad):
        self.edad = edad

    
    def setNota(self, notas):
        self.notas = notas



estudiante = Alumno("Andre", "202301")


estudiante.setAge(20)


estudiante.setNota([18, 17, 19])


estudiante.display()
