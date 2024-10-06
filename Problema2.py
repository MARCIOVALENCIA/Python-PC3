def obtener_calificaciones():
    while True:
        try:
            
            calificaciones_input = input("Ingrese una lista de calificaciones separadas por comas: ")
            
            
            calificaciones_str = calificaciones_input.split(',')
            
            
            calificaciones = [round(float(c.strip())) for c in calificaciones_str]
            
            
            return calificaciones

        except ValueError:
            
            print("Error: Asegúrese de ingresar solo números, sin letras. Intente nuevamente.")

if __name__ == '__main__':
    calificaciones = obtener_calificaciones()
    print(f"Calificaciones ingresadas: {calificaciones}")
