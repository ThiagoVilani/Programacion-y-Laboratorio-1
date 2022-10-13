import json
import re

def Cargar_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        data = json.load(archivo)
    return data