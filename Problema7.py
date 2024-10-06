import math

class Punto:
    def __init__(self, x=0, y=0):
      
        self.x = x
        self.y = y

 
    def __str__(self):
        return f"({self.x}, {self.y})"


    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante."
        elif self.x == 0 and self.y != 0:
            return "El punto está sobre el eje Y."
        elif self.x != 0 and self.y == 0:
            return "El punto está sobre el eje X."
        else:
            return "El punto está en el origen."


    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

  
    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
    
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final


    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

   
    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

 
    def area(self):
        return self.base() * self.altura()


punto1 = Punto(2, 3)
punto2 = Punto(5, 5)


print(f"Punto 1: {punto1}")
print(f"Punto 2: {punto2}")


print(punto1.cuadrante())
print(punto2.cuadrante())


vector = punto1.vector(punto2)
print(f"Vector entre Punto 1 y Punto 2: {vector}")


distancia = punto1.distancia(punto2)
print(f"Distancia entre Punto 1 y Punto 2: {distancia:.2f}")


rectangulo = Rectangulo(punto1, punto2)


print(f"Base del rectángulo: {rectangulo.base()}")
print(f"Altura del rectángulo: {rectangulo.altura()}")
print(f"Área del rectángulo: {rectangulo.area()}")
