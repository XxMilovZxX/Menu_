import json
from datetime import datetime

def guardar_estudiantes(estudiantes):
    with open('db_sys/estudiantes.json', 'w') as f:
        json.dump(estudiantes, f, indent=4)

def cargar_estudiantes():
    try:
        with open('db_sys/estudiantes.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def registrar_eliminacion(tipo, datos):
    archivo = 'db_sys/registros_eliminados.json'
    try:
        with open(archivo, 'r') as f:
            eliminados = json.load(f)
    except:
        eliminados = {}
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if tipo not in eliminados:
        eliminados[tipo] = []
    
    eliminados[tipo].append({
        "fecha": timestamp,
        "datos": datos
    })
    
    with open(archivo, 'w') as f:
        json.dump(eliminados, f, indent=4)

def validar_rut(rut):
    return len(rut) >= 8 and len(rut) <= 10

def validar_matricula(matricula):
    return len(matricula) == 8