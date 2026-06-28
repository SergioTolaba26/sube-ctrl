from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sube.json"


def leer_datos():
    with open(DATA_FILE, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_datos(datos):
    with open(DATA_FILE, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def obtener_saldo():
    datos = leer_datos()
    return datos["saldo"]


def obtener_tarifas():
    datos = leer_datos()
    return datos["tarifas"]


def obtener_movimientos():
    datos = leer_datos()
    return datos["movimientos"]