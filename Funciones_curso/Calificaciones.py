from Funciones_estudiantes.datos_estudiante import cargar_estudiantes, guardar_estudiantes

def registrar_calificacion():
    estudiantes = cargar_estudiantes()
    
    rut = input("Ingrese RUT del estudiante: ")
    if rut not in estudiantes:
        print("Estudiante no encontrado")
        return
    
    curso = input("Ingrese codigo del curso: ")
    if curso not in estudiantes[rut]["cursos"]:
        print("El estudiante no esta inscrito en este curso")
        return
    
    # Inicializar la estructura de calificaciones si no existe
    if "calificaciones" not in estudiantes[rut]:
        estudiantes[rut]["calificaciones"] = {}
    if curso not in estudiantes[rut]["calificaciones"]:
        estudiantes[rut]["calificaciones"][curso] = []
    
    while True:
        try:
            nota = float(input("Ingrese la nota (1.0 - 7.0): "))
            if nota < 1.0 or nota > 7.0:
                print("La nota debe estar entre 1.0 y 7.0")
                continue
            else:   
                # Agregar la nueva nota al listado de calificaciones del curso
                estudiantes[rut]["calificaciones"][curso].append(nota)
                print(f"Nota {nota} registrada")
            
                continuar = input("\n¿Desea ingresar otra nota? (si/no): ").lower()
                if continuar != 'si':
                    break
        except ValueError:
            print("Nota inválida")
    
    # Guardar los cambios
    guardar_estudiantes(estudiantes)

def calcular_promedio():
    estudiantes = cargar_estudiantes()
    rut = input("Ingrese RUT del estudiante: ")
    
    if rut not in estudiantes:
        print("Estudiante no encontrado")
        return
    
    calificaciones = estudiantes[rut].get("calificaciones", {})
    if not calificaciones:
        print("El estudiante no tiene notas registradas")
        return
    
    print("\nPromedios por curso:")
    for curso, notas in calificaciones.items():
        if notas:  # Verificar que haya notas en el curso
            promedio_curso = sum(notas) / len(notas)
            print(f"Curso {curso}: {promedio_curso:.1f}")
        else:
            print(f"Curso {curso}: Sin notas")
    
    # Calcular promedio general si hay notas
    todas_las_notas = [nota for notas_curso in calificaciones.values() for nota in notas_curso]
    if todas_las_notas:
        promedio_general = sum(todas_las_notas) / len(todas_las_notas)
        print(f"\nPromedio general: {promedio_general:.1f}")
    else:
        print("\nNo hay notas registradas para calcular el promedio general")