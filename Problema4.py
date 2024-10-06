class RECTANGULO:
    def __init__(self, largo, ancho):
      
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
      
        return self.largo * self.ancho



class CUADRADO(RECTANGULO):
    def __init__(self, lado):
       
        super().__init__(lado, lado)



rectangulo = RECTANGULO(10, 5)

cuadrado = CUADRADO(4)


print(f"El área del rectángulo de 10x5 es: {rectangulo.calcular_area()}")
print(f"El área del cuadrado de lado 4 es: {cuadrado.calcular_area()}")
