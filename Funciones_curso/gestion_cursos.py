from Funciones_curso.add_new_course import agregar_curso, cargar_cursos
from Funciones_curso.Calificaciones import registrar_calificacion, calcular_promedio
from Funciones_estudiantes.datos_estudiante import registrar_eliminacion
from Funciones_estudiantes.gestion_estudiante import cargar_estudiantes, guardar_estudiantes
import json

def listar_cursos():
    cursos = cargar_cursos()
    if not cursos:
        print("No hay cursos registrados")
        return
    
    print("\n///Lista de Cursos///")
    for codigo, datos in cursos.items():
        print(f"\nCodigo: {codigo}")
        print(f"Nombre: {datos["nombre"]}")
        print("Estudiantes:", len(datos["estudiantes"]))

def eliminar_curso():
    cursos = cargar_cursos()
    estudiantes = cargar_estudiantes()
    
    codigo = input("\nIngrese codigo del curso a eliminar: ")
    
    if codigo in cursos:
        # Obtener el curso antes de eliminarlo
        curso = cursos.pop(codigo)
        
        # Actualizar los estudiantes
        for rut in curso["estudiantes"]:
            if rut in estudiantes:
                # Eliminar el curso de la lista de cursos del estudiante
                if codigo in estudiantes[rut]["cursos"]:
                    estudiantes[rut]["cursos"].remove(codigo)
                # Eliminar las calificaciones del curso
                if codigo in estudiantes[rut].get("calificaciones", {}):
                    del estudiantes[rut]["calificaciones"][codigo]
        
        # Guardar los cambios
        with open('db_sys/cursos.json', 'w') as f:
            json.dump(cursos, f, indent=4)
        guardar_estudiantes(estudiantes)
        
        registrar_eliminacion("cursos", curso)
        print("Curso eliminado y registros de estudiantes actualizados")
    else:
        print("Curso no encontrado")

def mostrar_menu_cursos():
    while True:
            print("""\n///Gestion de Cursos///: (Ingrese una opcion del menu)
                    1. Agregar Curso
                    2. Listar Cursos
                    3. Eliminar Curso
                    4. Registrar Calificación
                    5. Calcular Promedio
                    6. Volver al Menú Principal""")
        
            opcion = int(input("\n"))
        
            if opcion == 1:
                agregar_curso()
            elif opcion == 2:
                listar_cursos()
            elif opcion == 3:
                eliminar_curso()
            elif opcion == 4:
                registrar_calificacion()
            elif opcion == 5:
                calcular_promedio()
            elif opcion == 6:
                break
            else:
                print("Opcion no valida")
        