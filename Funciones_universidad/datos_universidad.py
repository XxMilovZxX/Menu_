import json
import os

def guardar_universidad(datos):
    os.makedirs('db_sys', exist_ok=True)
    with open('db_sys/universidad.json', 'w') as f:
        json.dump(datos, f, indent=4)
    

def cargar_universidad():
    try:
        with open('db_sys/universidad.json', 'r') as f:
            return json.load(f)
    except:
        return {
            "nombre": "APLAPLAC",
            "sede_principal": "Concepcion",
            "sedes": ["Concepcion", "Material", "Biblioteca"],
        }