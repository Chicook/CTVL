import json
import gzip

def comprimir_y_guardar_datos(datos, archivo_salida):
    """
    Comprime los datos y los guarda en un archivo.
    
    :param datos: Datos a comprimir (dict).
    :param archivo_salida: Nombre del archivo de salida (str).
    """
    try:
        datos_serializados = json.dumps(datos).encode('utf-8')
        datos_comprimidos = gzip.compress(datos_serializados)
        with open(archivo_salida, 'wb') as archivo:
            archivo.write(datos_comprimidos)
        print(f"Datos comprimidos y guardados en {archivo_salida}")
    except Exception as e:
        print(f"Error al comprimir y guardar datos: {e}")

def cargar_y_descomprimir_datos(archivo_entrada):
    """
    Carga y descomprime los datos de un archivo.
    
    :param archivo_entrada: Nombre del archivo de entrada (str).
    :return: Datos descomprimidos (dict).
    """
    try:
        with open(archivo_entrada, 'rb') as archivo:
            datos_comprimidos = archivo.read()
        datos_descomprimidos = gzip.decompress(datos_comprimidos)
        return json.loads(datos_descomprimidos)
    except Exception as e:
        print(f"Error al cargar y descomprimir datos: {e}")
        return None

# código reservado por si
# hace falta mas adelante.

# import json
# import gzip

# def comprimir_y_guardar_datos(datos, archivo_salida):
   # datos_serializados = json.dumps(datos).encode('utf-8')
   # datos_comprimidos = gzip.compress(datos_serializados)
   # with open(archivo_salida, 'wb') as archivo:
   # archivo.write(datos_comprimidos)

# def cargar_y_descomprimir_datos(archivo_entrada):
  #  with open(archivo_entrada, 'rb') as archivo:
  #  datos_comprimidos = archivo.read()
  #  datos_descomprimidos = gzip.decompress(datos_comprimidos)
  # return json.loads(datos_descomprimidos)
