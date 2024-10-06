import Problema8


a = 10
b = 5
c = "texto"  

# Suma
print(f"Suma de {a} y {b}: {Problema8.suma(a, b)}")
print(f"Suma de {a} y {c}: {Problema8.suma(a, c)}")

# Resta
print(f"Resta de {a} y {b}: {Problema8.resta(a, b)}")
print(f"Resta de {a} y {c}: {Problema8.resta(a, c)}")

# Producto
print(f"Producto de {a} y {b}: {Problema8.producto(a, b)}")
print(f"Producto de {a} y {c}: {Problema8.producto(a, c)}")

# División
print(f"División de {a} entre {b}: {Problema8.division(a, b)}")
print(f"División de {a} entre 0: {Problema8.division(a, 0)}")
print(f"División de {a} entre {c}: {Problema8.division(a, c)}")
