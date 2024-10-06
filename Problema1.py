def obtener_combustible():
    while True:
        try:
            
            fraccion = input("Ingrese una fracción en formato X/Y (Ejemplo 3/4): ")
            x, y = fraccion.split('/')
            
            
            x = int(x)
            y = int(y)

            
            if x > y:
                print("Error: X debe ser menor o igual a Y. Intente nuevamente.")
                continue
            if y == 0:
                raise ZeroDivisionError


            porcentaje = round((x / y) * 100)


            if porcentaje < 1:
                return "E"
            elif porcentaje > 99:
                return "F"
            else:
                return f"{porcentaje}%"

        except ValueError:
            print("Error: Solo se permiten números enteros. Intente nuevamente.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser cero. Intente nuevamente.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}. Intente nuevamente.")


if __name__ == '__main__':
    resultado = obtener_combustible()
    print(f"Output: {resultado}")
