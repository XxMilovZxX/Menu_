from Funciones_estudiantes.datos_estudiante import (
    guardar_estudiantes, cargar_estudiantes,              #Importamos las funcione snecesarias de los demas modulos
    registrar_eliminacion, validar_rut, validar_matricula
)
from Funciones_curso.add_new_course import cargar_cursos, guardar_cursos

def inscribir_curso():
    estudiantes = cargar_estudiantes()  #Llamamos las funciones para cargar los datos
    cursos = cargar_cursos()
    
    print("\n///Inscribir estudiante en curso///")
    rut = input("Ingrese rut del estudiante: ")       
    
    if rut not in estudiantes:
        print("Estudiante no encontrado") #Si el estudiante no esta en lo registrado en el rut, entonces se sale de la funcion y lanza ese mensaje
        return
        
    if not cursos:
        print("No hay cursos disponibles") #Si no encuentra cursos, lanza ese mensaje y sale de la funcion
        return
        
    print("\nCursos disponibles: ")
    for codigo, datos in cursos.items():                       #Te muestra por pantalla los nombres de estos cursos y sus codigos
        print(f"Codigo: {codigo} - Nombre: {datos['nombre']}")
    
    codigo_curso = input("\nIngrese codigo del curso: ")
    if codigo_curso not in cursos:
        print("Curso no encontrado")                   #Si el codigo del curso es incorrecto, entonces te lanza ese mensaje y sale de la funcion
        return
        
    if codigo_curso in estudiantes[rut]["cursos"]:
        print("El estudiante ya está inscrito en este curso")   #Si el estudiante ya tiene ese curso, entonces el codigo lo identifica y lanza ese mensaje para salir de la funcion
        return
    
    # Actualiza la lista de cursos del estudiante
    estudiantes[rut]["cursos"].append(codigo_curso)
    # Actualiza la lista de estudiantes del curso
    cursos[codigo_curso]["estudiantes"].append(rut)
    
    # Guarda los cambios en ambos archivos
    guardar_estudiantes(estudiantes)
    guardar_cursos(cursos)
    
    print("Estudiante inscrito exitosamente en el curso")
    
def agregar_estudiante():
    estudiantes = cargar_estudiantes() #llama la funcion para cargar los datos del estudiante
    
    rut = input("Ingrese Rut del estudiante: (Ingrese sin puntos y con guion)\n")
    print("\n///Agregar Nuevo Estudiante///")
    if not validar_rut(rut):
        print("El rut es incorrecto") #Se llama a la funcion validar rut para identificar si es correcto
        return
    
    if not validar_matricula(matricula):
        matricula = input("Ingrese matricula: (8 digitos)\n")
        print("La matricula es incorrecta") #Se llama a la funcion validar matricula para identificar si es correcto
        return
    
    nombre = input("Ingrese nombre completo: ")
    #Se guardan los datos en una biblioteca
    estudiante = {
        "numero_identificacion_nombre": (rut, matricula, nombre),
        "cursos": [],                                              
        "calificaciones": {}
    }
    
    estudiantes[rut] = estudiante
    guardar_estudiantes(estudiantes) #Se guardan estos nuevos datos
    print("Estudiante agregado")

def listar_estudiantes():
    estudiantes = cargar_estudiantes() #Llama la funcion para cargar los datos
    if not estudiantes:
        print("No hay estudiantes registrados") #Si no encuentra estudiantes, entonces te lanza ese mensaje y sale de la funcion
        return
    
    print("\n///Lista de Estudiantes///")
    for rut, datos in estudiantes.items():
        try:
            print(f"\nRut, matricula y nombre: {datos['numero_identificacion_nombre']}")  #Imprime por pantalla los datos del estudiante
            print("Cursos:", ", ".join(datos["cursos"]) if datos["cursos"] else "Sin cursos") #En caso de no tener cursos registrados, escribe "Sin cursos"
            
            if datos["calificaciones"]:
                print("Calificaciones:")                   #Si el estudiante tiene notas registradas entonces los busca
                for curso, notas in datos["calificaciones"].items():
                    if notas:
                        promedio = sum(notas) / len(notas)
                        print(f"  {curso}: {notas} (Promedio: {promedio:.1f})") #Les saca el promedio
                    else:
                        print(f"  {curso}: Sin notas")
            else:
                print("No hay notas registradas")
        except KeyError as e:
            print(f"Error en los datos del estudiante con RUT {rut}: {e}") #Cuando el usuario se equivoca, lanza un mensaje de error especifico 
            continue

def eliminar_estudiante():
    estudiantes = cargar_estudiantes() #Llama la funcion para cargar los datos del estudiante
    rut = input("\nIngrese Rut del estudiante que quiere eliminar: ")
    
    if rut in estudiantes: #Si el rut existe en los estudiantes
        estudiante = estudiantes.pop(rut) #Entonces elimina el estudiante en esepcifico indicado por el rut
        guardar_estudiantes(estudiantes)  #Guarda la accion recien realizada
        registrar_eliminacion("estudiantes", estudiante) 
        print("Estudiante eliminado") #Indica que el estudiante se a eliminado
    else:
        print("Estudiante no encontrado") #El estudiante no fue encontrado

def mostrar_menu_estudiantes():
    while True:
        try:#Menu de gestion de estudiantes 
            print("""\n///Gestion de Estudiantes///: (Ingrese una opcion del menu)
                1. Agregar Estudiante
                2. Listar Estudiantes
                3. Eliminar Estudiante
                4. Inscribir Estudiante en un curso
                5. Volver al Menu Principal""")
        
            opcion = int(input("\n"))
        
            if opcion == 1:
                agregar_estudiante()
            elif opcion == 2:
                listar_estudiantes()
            elif opcion == 3:
                eliminar_estudiante()
            elif opcion == 4:
                inscribir_curso()
            elif opcion == 5:
                break
            else:
                print("Opcion no valida")
                continue
        except:                                     #Indicacion de errores en caso de que el usuario se equivoque
            print("Error, ingrese una opcion valida")
            continue