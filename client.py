import requests

AR_URL = "http://44.197.32.169:8081"

def get_tareas():
    response = requests.get(f'{AR_URL}/tareas')
    status = response.status_code 

    if status == 200:
        return response.json()
    else:
        print("No fue posible obtener la lista de tareas\n")


def add_tarea(AR_tarea, AR_descripcion):
    data = {"nombre": AR_tarea, "descripcion": AR_descripcion, "hecha" : "no"}
    response = requests.post(f'{AR_URL}/tareas', json=data)   
    status = response.status_code 

    if status == 200:
        print("Tarea agregada correctamente\n")

    else:
        print("No fue posible agregar la tarea\n")


def update_tarea(AR_tarea, AR_completada):
    data = {
        "nombre": AR_tarea, 
        "hecha":AR_completada
        }

    response = requests.put(f'{AR_URL}/tareas', json=data)
    status = response.status_code

    if status == 200:
        print("Tarea actualizada correctamente\n")
    
    elif status == 404:
        print("Tarea no encontrada\n")


def delete_tarea(AR_tarea):
    data = {"nombre" : AR_tarea}
    response = requests.delete(f'{AR_URL}/tareas', json=data)
    status = response.status_code
    
    if status == 404:
        print("error 404: no fue posible encontrar la tarea\n")
        
    elif status == 200:
        print("La tarea fue eliminada\n")


def mostrar_tareas_pendientes():
    response = requests.get(f'{AR_URL}/tareas')
    tareas = response.json()

    print("Tareas pendientes -> ")
    for tarea in tareas:
        if tarea["hecha"] == "no":
            print(tarea["nombre"] + ": " + tarea["descripcion"])
    print("");


def mostrar_tareas_hechas():
    response = requests.get(f'{AR_URL}/tareas')
    tareas = response.json()

    print("Tareas hechas -> ")
    for tarea in tareas:
        if tarea["hecha"] == "si":
            print(tarea["nombre"] + ": " + tarea["descripcion"])
    print("");


def mostrar_descripcion(nombre_tarea):
    response = requests.get(f'{AR_URL}/tareas')
    tareas = response.json()

    for tarea in tareas:
        if tarea["nombre"] == nombre_tarea:
            print(tarea["nombre"] + ": Descripción: " + tarea["descripcion"])
    print("");


def mostrar_menu():
    print("Bienvenido al menú de gestión de tareas:")
    print("1. Obtener lista de tareas")
    print("2. Agregar nueva tarea")
    print("3. Actualizar tarea existente")
    print("4. Eliminar tarea")
    print("5. Mostrar tareas pendientes")
    print("6. Mostrar tareas hechas")
    print("7. Mostrar descripcion")
    print("8. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            print("\nLista de tareas:")
            tareas = get_tareas()
            for tarea in tareas:
                print(tarea["nombre"])  # Imprime solo el nombre de la tarea
            print("")
            

        elif opcion == "2":
            add_tarea(
                input("\nIngrese el nombre de la nueva tarea: "), 
                input("Ingrese la descripción de la nueva tarea: ")
                )

        elif opcion == "3":
            update_tarea(
                input("\nIngrese el nombre de la tarea que desea actualizar: "),
                input("¿La tarea está hecha?: ")
                )

        elif opcion == "4":
            delete_tarea(
                input("\nIngrese el nombre de la tarea que desea eliminar: "))
        
        elif opcion == "5":
            print("")
            mostrar_tareas_pendientes()

        elif opcion == "6":
            print("")
            mostrar_tareas_hechas()

        elif opcion == "7":
            mostrar_descripcion(
                input("\nIngrese el nombre de la tarea: "))

        elif opcion == "8":
            print("\nSaliendo del programa...")
        
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
        