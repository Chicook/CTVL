import hashlib
import time
import prb4

blockchain = []

def crear_wallet():
    """
    Crea una nueva wallet con un ID único.
    """
    wallet_id = "wbrs" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    wallet = {'id': wallet_id, 'timestamp': time.time()}
    prb4.add_block(wallet)
    return wallet

def validar_registro(forks):
    """
    Valida un registro basado en el número de forks.
    """
    valor = forks * 2  # Ejemplo de validación
    registro = {'forks': forks, 'valor': valor, 'timestamp': time.time()}
    prb4.add_block(registro)
    return valor

def registrar_en_blockchain(data):
    """
    Registra datos en la blockchain.
    """
    prb4.add_block(data)
