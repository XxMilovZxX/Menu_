import json

def guardar_cursos(cursos):
    with open('db_sys/cursos.json', 'w') as f:
        json.dump(cursos, f, indent=4)

def cargar_cursos():
    try:
        with open('db_sys/cursos.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def agregar_curso():
    cursos = cargar_cursos()
    
    codigo = input("Ingrese codigo del curso: ")
    if codigo in cursos:
        print("El curso ya existe")
        return
    
    nombre = input("Ingrese nombre del curso: ")
    
    curso = {
        "codigo": codigo,
        "nombre": nombre,
        "estudiantes": []
    }
    
    cursos[codigo] = curso
    guardar_cursos(cursos)
    print("Curso agregado")