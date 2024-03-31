from requests import put, get, post, delete

IP = "127.0.0.1"
IP = "44.197.32.169"
PORT = "8081"
URL = f'http://{IP}:{PORT}'


def get_tareas():
    response = get(f'{URL}/tareas')
    status = response.status_code 

    if status == 200:
        return response.json()
    else:
        print("No fue posible obtener la lista de tareas")


def add_tarea(nombre: str, descripcion: str):
    data = {"nombre": nombre, "descripcion": descripcion, "hecha" : "no"}
    response = post(f'{URL}/tareas', json=data)   
    status = response.status_code 

    if status == 200:
        print("Tarea agregada correctamente")

    else:
        print("No fue posible agregar la tarea")


def update_tarea(nombre: str, completada: str):
    data = {
        "nombre": nombre, 
        "hecha": completada,
        }

    response = put(f'{URL}/tareas', json=data)
    status = response.status_code

    if status == 200:
        print("Tarea actualizada correctamente")
    
    elif status == 404:
        print("Tarea no encontrada")


def delete_tarea(nombre: str):
    data = {"nombre" : nombre}
    response = delete(f'{URL}/tareas', json=data)
    status = response.status_code
    
    if status == 404:
        print("error 404: no fue posible encontrar la tarea")

    elif status == 200:
        print("La tarea fue eliminada")


def imprimir_tarea(tarea):
    print(
        "%s, hecha: %s, %s" 
        %(tarea["nombre"], tarea["hecha"], tarea["descripcion"] )
        )


def imprimir_lista_tareas():
    print("\nLista de tareas:")
    tareas = get_tareas()
    for tarea in tareas:
        imprimir_tarea(tarea)


def mostrar_filtrar_tareas(key: str, data: str):
    tareas = get_tareas()

    for tarea in tareas:
        if tarea[key] == data:
            imprimir_tarea(tarea)


def mostrar_tareas_pendientes():
    tareas = get_tareas()

    print("Tareas pendientes: ")
    mostrar_filtrar_tareas("hecha","no")


def mostrar_tareas_hechas():
    tareas = get_tareas()

    print("Tareas hechas: ")
    mostrar_filtrar_tareas("hecha","si")


def mostrar_tarea(nombre_tarea: str):
    tareas = get_tareas()
    mostrar_filtrar_tareas("nombre", nombre_tarea)
    

def mostrar_menu():
    print("\nBienvenido al menú de gestión de tareas:")
    print("1. Obtener lista de tareas")
    print("2. Agregar nueva tarea")
    print("3. Actualizar tarea existente")
    print("4. Eliminar tarea")
    print("5. Mostrar tareas pendientes")
    print("6. Mostrar tareas hechas")
    print("7. Mostrar descripcion")
    print("8. Salir\n")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            imprimir_lista_tareas()
            
        elif opcion == "2":
            add_tarea(
                input("Ingrese el nombre de la nueva tarea: "), 
                input("Ingrese la descripción de la nueva tarea: ")
                )

        elif opcion == "3":
            update_tarea(
                input("Ingrese el nombre de la tarea que desea actualizar: "),
                input("¿La tarea está hecha?: ")
                )

        elif opcion == "4":
            delete_tarea(
                input("Ingrese el nombre de la tarea que desea eliminar: "))
        
        elif opcion == "5":
            mostrar_tareas_pendientes()

        elif opcion == "6":
            mostrar_tareas_hechas()

        elif opcion == "7":
            mostrar_descripcion(
                input("Ingrese el nombre de la tarea: "))

        elif opcion == "8":
            print("Saliendo del programa...")
            break;
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
        