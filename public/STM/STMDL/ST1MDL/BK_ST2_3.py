# BK_ST2_3.py - Funciones para la sincronización entre nodos

import requests
import json
from BK_ST2_1 import cargar_blockchain, guardar_blockchain

# Función para obtener la lista de nodos desde la configuración
def obtener_nodos():
    with open("config.json", "r") as archivo:
        return json.load(archivo)["nodos"]

# Función para sincronizar la blockchain con otros nodos
def sincronizar_blockchain():
    nodos = obtener_nodos()
    for nodo in nodos:
        try:
            response = requests.get(f"{nodo}/blockchain")
            if response.status_code == 200:
                blockchain_remota = response.json()
                blockchain_local = cargar_blockchain()

                # Comparar y actualizar la blockchain si es necesario
                if len(blockchain_remota) > len(blockchain_local):
                    guardar_blockchain(blockchain_remota)
                    return blockchain_remota
                return blockchain_local
        except:
            continue

    return cargar_blockchain()  # Si no se pudo sincronizar, se devuelve la blockchain local.
