import os, json
os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)
    
def menu_general():
    os.system('cls')
    print("1. Crear Empleado")
    print("2. Actualizar Empleado")
    print("3. Eliminar Empleado")
    print("4. Listar Empleados")
    print("5. Salir")

def seleccionar_opcion(max_option):
    while True:
        opcion = 0
        try:
            opcion = int(input("Seleccione una opcion >>> "))
        except:
            pass
        if opcion < 1 or opcion > max_option:
            input("Opcion invalida. Enter para continuar...")
        else:
            return opcion
    
def iniciar_programa():
    while True:
        menu_general()
        opcion = seleccionar_opcion(5)
        if opcion == 1:
            print("1. Crear Empleado")


        elif opcion ==2:
            print("2. Actualizar Empleado")

        elif opcion ==3:
            print("3. Eliminar Empleado")

        elif opcion ==4:
            print("4. Listar Empleados")

        elif opcion ==5:
            print("5. Salir")

        empleados = cargar_json('empleados.json')
        print(empleados)

iniciar_programa()