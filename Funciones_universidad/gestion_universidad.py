from .datos_universidad import cargar_universidad, guardar_universidad
from Funciones_estudiantes.datos_estudiante import registrar_eliminacion

def listar_sedes():
    universidad = cargar_universidad() #Llama la funcion que trae los datos
    sedes = universidad.get("sedes", [])
    
    print("\n/// Sedes APLAPLAC ///")
    if sedes:  # Verifica que haya sedes registradas
        for sede in sedes:
            print(f"- {sede}")
    else:
        print("No hay sedes registradas.")

def eliminar_sede():
    universidad = cargar_universidad()
    sede = input("\nIngrese el nombre de la sede que desea eliminar: ")
    
    if sede == "Concepción":
        print("No se puede eliminar la sede principal")
        return
    
    if sede in universidad.get("sedes", []):
        universidad["sedes"].remove(sede)
        guardar_universidad(universidad)
        registrar_eliminacion("sedes", {"sede": sede})
        print("Sede eliminada")
    else:
        print("La sede ingresada no fue encontrada")

def mostrar_menu_universidad():
    while True:
        try:
            print("""\n/// Gestión de Universidad ///: Seleccione una opción:
                    1. Agregar Sede
                    2. Listar Sedes
                    3. Eliminar Sede
                    4. Volver al Menú Principal""")
            
            opcion = int(input(""))
            
            if opcion == 1:
                universidad = cargar_universidad()
                sedes = input("Ingrese el nombre de la nueva sede: ")
    
                if sedes in universidad["sedes"]:
                    print(f"La sede '{sedes}' ya existe. Por favor, ingrese una sede diferente.")
                    continue
                if sedes not in universidad["sedes"]:
                    print("La sede no se ingreso")
                    continue
    
                universidad["sedes"].append(sedes)
                guardar_universidad(universidad)
                print(f"La sede '{sedes}' ha sido agregada a la universidad.")
                break
            elif opcion == 2:
                listar_sedes()
            elif opcion == 3:
                eliminar_sede()
            elif opcion == 4:
                break
            else:
                print("Opcion no valida. Intente nuevamente.")
        except ValueError:
            print("Error, Ingrese un numero valido para seleccionar una opcion.")