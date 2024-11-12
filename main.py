import os
import json
from datetime import datetime
from Funciones_estudiantes.gestion_estudiante import mostrar_menu_estudiantes
from Funciones_curso.gestion_cursos import mostrar_menu_cursos
from Funciones_universidad.gestion_universidad import mostrar_menu_universidad

def cargar_datos():
    if not os.path.exists('db_sys'):         #Crea las bodegas de db_sys en caso de que no existan
        os.makedirs('db_sys')
    
    archivos = {
        'estudiantes': 'db_sys/estudiantes.json',
        'cursos': 'db_sys/cursos.json',             #Bodegas de Json que guardan la informacion
        'universidad': 'db_sys/universidad.json',
        'eliminados': 'db_sys/registros_eliminados.json'
    }
    
    for archivo in archivos.values():
        if not os.path.exists(archivo):             #Esta parte del codigo verifica si existe, y sino, entocences crea el espacio vacio en las bodegas
            with open(archivo, 'w') as f:
                json.dump({}, f)

def registrar_cierre():
    with open('registro_cierre.txt', 'a') as f:
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')   #Esta funcion del codigo genera un archivo txt. que registra cuando cierra el programa
        f.write(f'Cierre del programa: {fecha_hora}\n')

def menu_principal():
    while True:
        try: #Menu principal de acciones
            print("""Menu de gestion principal: (Ingrese una opcion del menu)
                1. Gestion de Estudiantes
                2. Gestion de Cursos                                            
                3. Gestion de Universidad
                4. Salir""")
        
        
            opcion = int(input("\n"))
            if opcion == 1:
                mostrar_menu_estudiantes()
            elif opcion == 2:
                mostrar_menu_cursos()                   #Aqui elegimos una opcion del menu
            elif opcion == 3:
                mostrar_menu_universidad()
            elif opcion == 4:
                print("Cerrado")
                registrar_cierre()
                break 
            else:
                print("Error, ingreso una opcion invalida")
                continue
        except:                                          #Verificacion de errores, en caso de que el usuario se equivoque, se repite el menu
            print("Error, ingreso una opcion invalida")
            continue

if __name__ == "__main__":
    cargar_datos()              #Aqui se identifica un "main" en donde cargaremos los archivos json y el menu principal
    menu_principal()