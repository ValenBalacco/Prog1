# Lista de tuplas de pasajeros
pasajeros = []

# Lista de tuplas de ciudades y países
ciudades = []

while True:
    print("\nMenú de Operaciones:")
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Ver a qué ciudad viaja un pasajero por DNI")
    print("4. Mostrar cantidad de pasajeros que viajan a una ciudad")
    print("5. Ver a qué país viaja un pasajero por DNI")
    print("6. Mostrar cantidad de pasajeros que viajan a un país")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del pasajero: ")
        dni = int(input("Ingrese el DNI del pasajero: "))
        destino = input("Ingrese el destino del pasajero: ")
        pasajeros.append((nombre, dni, destino))
        print("Pasajero agregado exitosamente.")

    elif opcion == "2":
        ciudad = input("Ingrese el nombre de la ciudad: ")
        pais = input("Ingrese el país al que pertenece la ciudad: ")
        ciudades.append((ciudad, pais))
        print("Ciudad agregada exitosamente.")

    elif opcion == "3":
        dni_pasajero = int(input("Ingrese el DNI del pasajero: "))
        encontrado = False
        for pasajero in pasajeros:
            if pasajero[1] == dni_pasajero:
                print(f"{pasajero[0]} viaja a {pasajero[2]}.")
                encontrado = True
                break
        if not encontrado:
            print("Pasajero no encontrado.")

    elif opcion == "4":
        ciudad_destino = input("Ingrese el nombre de la ciudad: ")
        cantidad = sum(1 for pasajero in pasajeros if pasajero[2] == ciudad_destino)
        print(f"{cantidad} pasajeros viajan a {ciudad_destino}.")

    elif opcion == "5":
        dni_pasajero = int(input("Ingrese el DNI del pasajero: "))
        encontrado = False
        for pasajero in pasajeros:
            if pasajero[1] == dni_pasajero:
                for ciudad, pais in ciudades:
                    if ciudad == pasajero[2]:
                        print(f"{pasajero[0]} viaja a {pais}.")
                        encontrado = True
                        break
        if not encontrado:
            print("Pasajero no encontrado.")

    elif opcion == "6":
        pais_destino = input("Ingrese el nombre del país: ")
        cantidad = sum(1 for pasajero in pasajeros for ciudad, pais in ciudades if ciudad == pasajero[2] and pais == pais_destino)
        print(f"{cantidad} pasajeros viajan a {pais_destino}.")

    elif opcion == "7":
        print("Saliendo del programa.")
        break
        

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")



def obtener_domicilios_facturacion(compras):
    domicilios_facturacion = {}  # Un diccionario para almacenar los domicilios únicos

    for compra in compras:
        cliente, dia, monto, domicilio = compra
        if cliente not in domicilios_facturacion:
            domicilios_facturacion[cliente] = set()  # Inicializa un conjunto vacío para el cliente
        domicilios_facturacion[cliente].add(domicilio)  # Agrega el domicilio al conjunto

    return domicilios_facturacion

# Ejemplo de lista de compras
compras = [('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'),
           ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),
           ('Nuria Costa', 15, 567.8, 'Calle 1 - 456')]

domicilios = obtener_domicilios_facturacion(compras)

for cliente, domicilios_cliente in domicilios.items():
    print(f"Cliente: {cliente}")
    print("Domicilios de facturación:")
    for domicilio in domicilios_cliente:
        print(domicilio)
    print()

# Diccionario con los datos iniciales de los socios fundadores
socios = {
    1: {"nombre": "Amanda Núñez", "ingreso": "17/03/2009", "cuota_al_dia": True},
    2: {"nombre": "Bárbara Molina", "ingreso": "17/03/2009", "cuota_al_dia": True},
    3: {"nombre": "Lautaro Campos", "ingreso": "17/03/2009", "cuota_al_dia": True}
}

# Función para informar la cantidad de socios
def cantidad_socios():
    return len(socios)

# Función para registrar que un socio ha pagado todas las cuotas adeudadas
def pagar_cuotas(numero_socio):
    if numero_socio in socios:
        socios[numero_socio]["cuota_al_dia"] = True
        print(f"El socio n°{numero_socio} ha pagado todas las cuotas adeudadas.")
    else:
        print("Socio no encontrado.")

# Función para modificar la fecha de ingreso de los socios ingresados el 13/03/2018
def modificar_fecha_ingreso():
    for numero_socio, datos in socios.items():
        if datos["ingreso"] == "13/03/2018":
            datos["ingreso"] = "14/03/2018"

# Función para dar de baja a un socio por nombre y apellido
def dar_de_baja(nombre_apellido):
    for numero_socio, datos in list(socios.items()):
        if datos["nombre"].lower() == nombre_apellido.lower():
            del socios[numero_socio]
            print(f"{nombre_apellido} ha sido dado de baja.")
            return
    print("Socio no encontrado.")

# Función para imprimir el listado de socios completo
def imprimir_listado_socios():
    for numero_socio, datos in socios.items():
        print(f"Socio n°{numero_socio}:")
        print(f"Nombre: {datos['nombre']}")
        print(f"Fecha de ingreso: {datos['ingreso']}")
        estado_cuota = "al día" if datos["cuota_al_dia"] else "en deuda"
        print(f"Estado de cuota: {estado_cuota}")
        print()

# Menú interactivo
while True:
    print("\nMenú de Operaciones:")
    print("1. Informar cantidad de socios")
    print("2. Registrar pago de cuotas de un socio")
    print("3. Modificar la fecha de ingreso de socios")
    print("4. Dar de baja a un socio")
    print("5. Imprimir listado de socios")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Total de socios en el club: {cantidad_socios()}")

    elif opcion == "2":
        numero_socio = int(input("Ingrese el número de socio que ha pagado las cuotas: "))
        pagar_cuotas(numero_socio)

    elif opcion == "3":
        modificar_fecha_ingreso()
        print("Fecha de ingreso modificada para socios ingresados el 13/03/2018.")

    elif opcion == "4":
        nombre_apellido = input("Ingrese el nombre y apellido del socio a dar de baja: ")
        dar_de_baja(nombre_apellido)

    elif opcion == "5":
        imprimir_listado_socios()

    elif opcion == "6":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
