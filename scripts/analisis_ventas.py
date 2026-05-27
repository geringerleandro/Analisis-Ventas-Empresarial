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

# BLOQUE 2: CALCULOS Y ANALISIS DE VENTAS

def calcular_total(ventas):
    """Recibe la lista de ventas y retorna la suma total de todos los montos."""
    total = 0
    for venta in ventas:
        total += venta["monto"]
    return total

def calcular_promedio(ventas):
    """Recibe la lista de ventas y retorna el promedio diario de ventas."""
    # Dividimos el total por la cantidad de registros para obtener el promedio diario
    return calcular_total(ventas) / len(ventas)

def calcular_maximo(ventas):
    """Recibe la lista de ventas y retorna el diccionario correspondiente al dia de mayor venta."""
    maximo = ventas[0]
    for venta in ventas:
        # Si encontramos un monto mayor al actual, actualizamos el maximo
        if venta["monto"] > maximo["monto"]:
            maximo = venta
    return maximo

def calcular_ventas_por_mes(ventas):
    """
    Recibe la lista de ventas y agrupa los montos por mes.
    Retorna un diccionario donde la clave es el mes (MM) y el valor es la suma de ventas de ese mes.
    """
    ventas_por_mes = {}
    for venta in ventas:
        # La fecha tiene formato YYYY-MM-DD, cortamos los caracteres del mes
        mes = venta["fecha"][5:7]
        if mes in ventas_por_mes:
            ventas_por_mes[mes] += venta["monto"]
        else:
            # Si el mes no existe en el diccionario, lo creamos con el monto actual
            ventas_por_mes[mes] = venta["monto"]
    return ventas_por_mes

def calcular_mes_mayor_venta(ventas_por_mes):
    """Recibe el diccionario de ventas por mes y retorna el mes con mayor volumen de ventas."""
    mes_mayor = None
    mayor_monto = 0
    for mes, monto in ventas_por_mes.items():
        if monto > mayor_monto:
            mayor_monto = monto
            mes_mayor = mes
    return mes_mayor, mayor_monto

# Ejecutamos los calculos y mostramos los resultados
total = calcular_total(ventas)
promedio = calcular_promedio(ventas)
maximo = calcular_maximo(ventas)
ventas_por_mes = calcular_ventas_por_mes(ventas)
mes_mayor, monto_mes_mayor = calcular_mes_mayor_venta(ventas_por_mes)

print(f"Ventas totales del año: ${total:.2f}")
print(f"Promedio diario de ventas: ${promedio:.2f}")
print(f"Dia con mayor venta: {maximo['fecha']} con ${maximo['monto']:.2f}")
print(f"Mes con mayor volumen de ventas: {mes_mayor} con ${monto_mes_mayor:.2f}")

# BLOQUE 3: GENERACION DEL GRAFICO

# Importamos matplotlib, la librería estándar de Python para generar gráficos
import matplotlib.pyplot as plt

# Extraemos las fechas y montos de la lista de diccionarios para usarlos en el gráfico
fechas = []
montos = []
for venta in ventas:
    fechas.append(venta["fecha"])
    montos.append(venta["monto"])

# Creamos la figura y definimos su tamaño en pulgadas
plt.figure(figsize=(14, 5))

# Graficamos las fechas en el eje X y los montos en el eje Y
plt.plot(fechas, montos)

# Reducimos las etiquetas del eje X para que no se superpongan entre sí
plt.xticks(fechas[::30], rotation=45) # (Luis)Mostramos una etiqueta cada 30 dias para evitar superposicion en el eje X

# Agregamos títulos y etiquetas a los ejes
plt.title("Evolución de ventas diarias - 2024")
plt.xlabel("Fecha")
plt.ylabel("Monto ($)")

plt.tight_layout()

# Guardamos el gráfico en la carpeta /resultados del repositorio
plt.savefig("/content/Analisis-Ventas-Empresarial/resultados/grafico_ventas.png")
print("Gráfico guardado correctamente en /resultados")
