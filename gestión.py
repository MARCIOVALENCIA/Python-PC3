

class GestionBiblioteca:
    def __init__(self):

        self.libros = []

    def agregar_libro(self, libro):

        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def listar_libros(self):

        if self.libros:
            for libro in self.libros:
                print(libro)
        else:
            print("No hay libros en la biblioteca.")

    def buscar_por_titulo(self, titulo):
      
        encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")

    def buscar_por_autor(self, autor):
    
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros del autor '{autor}'.")
