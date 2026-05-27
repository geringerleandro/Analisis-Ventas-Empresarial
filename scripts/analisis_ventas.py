# El comando %%writefile de la linea anterior le indica a Colab que guarde el contenido de esta celda en el archivo especificado

# BLOQUE 1: LECTURA Y PREPARACIÓN DE DATOS

def leer_ventas(ruta_archivo):
    """
    Recibe la ruta del archivo CSV y lo lee línea por línea.
    Retorna una lista de diccionarios con los campos: id, fecha y monto.
    """
    ventas = []
    with open(ruta_archivo, "r") as archivo:
        encabezado = next(archivo) # Descartamos la línea de encabezados
        for linea in archivo:
            # Limpiamos el salto de línea y separamos por coma
            linea_procesada = linea.strip().split(",")
            venta = {
                "id": linea_procesada[0],
                "fecha": linea_procesada[1],
                "monto": float(linea_procesada[2])
            }
            ventas.append(venta)
    return ventas

# Cargamos los datos usando la ruta desde la raíz del repositorio
ventas = leer_ventas("/content/Analisis-Ventas-Empresarial/data/sales_sample_2024.csv")
print(f"Registros cargados correctamente: {len(ventas)}")
