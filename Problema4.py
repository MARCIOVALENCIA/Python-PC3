class RECTANGULO:
    def __init__(self, largo, ancho):
        # Inicializar los atributos largo y ancho
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        # Calcular el área utilizando la fórmula del área del rectángulo: largo * ancho
        return self.largo * self.ancho


# La clase CUADRADO hereda de RECTANGULO
class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        # Inicializar el lado (largo y ancho son iguales en un cuadrado)
        super().__init__(lado, lado)


# Crear un objeto de tipo RECTANGULO
rectangulo = RECTANGULO(10, 5)
# Crear un objeto de tipo CUADRADO
cuadrado = CUADRADO(4)

# Calcular y mostrar el área de cada objeto
print(f"El área del rectángulo de 10x5 es: {rectangulo.calcular_area()}")
print(f"El área del cuadrado de lado 4 es: {cuadrado.calcular_area()}")
