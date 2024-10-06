class Producto:
    def __init__(self, nombre, precio, año):
        
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
   
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Año: {self.año}"


class Catálogo:
    def __init__(self):
        
        self.productos = []

    
    def agregar_producto(self, producto):
        self.productos.append(producto)

   
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

  
    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)

   
    def filtrar_por_precio(self, precio_min, precio_max):
        print(f"Productos con precio entre ${precio_min} y ${precio_max}:")
        for producto in self.productos:
            if precio_min <= producto.precio <= precio_max:
                print(producto)



producto1 = Producto("Filtro de aire", 50, 2021)
producto2 = Producto("Bujía", 30, 2020)
producto3 = Producto("Amortiguador", 100, 2021)


catalogo = Catálogo()


catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)


print("Todos los productos en el catálogo:")
catalogo.mostrar_productos()


catalogo.filtrar_por_año(2021)


catalogo.filtrar_por_precio(30, 80)
