# Ejercicio 1
numeros = []
while True:
    numero = int(input("Ingresa un número (0 para finalizar): "))
    if numero == 0:
        break
    numeros.append(numero)

# Ejercicio 2
numero_a_eliminar = int(input("Ingresa un número a eliminar: "))
if numero_a_eliminar in numeros:
    numeros.remove(numero_a_eliminar)
else:
    print("El número no se encuentra en la lista y no se puede eliminar.")

# Ejercicio 3
sumatoria = sum(numeros)
print(f"La sumatoria de los números en la lista es: {sumatoria}")

# Ejercicio 4
numero_limite = int(input("Ingresa un número límite: "))
nueva_lista = [n for n in numeros if n < numero_limite]
print("Nueva lista con elementos menores que el número límite:")
for elemento in nueva_lista:
    print(elemento)

# Ejercicio 5
conteos = [(n, numeros.count(n)) for n in set(numeros)]
print("Lista de tuplas con números y sus conteos:")
print(conteos)

#Ejercicio 6
nombres_primaria = set()
nombres_secundaria = set()

while True:
    nombre = input("Ingresa el nombre de un alumno de nivel primario (o 'x' para finalizar): ")
    if nombre == 'x':
        break
    nombres_primaria.add(nombre)

while True:
    nombre = input("Ingresa el nombre de un alumno de nivel secundario (o 'x' para finalizar): ")
    if nombre == 'x':
        break
    nombres_secundaria.add(nombre)

todos_los_nombres = nombres_primaria.union(nombres_secundaria)
print("Nombres de todos los alumnos sin repeticiones:")
print(todos_los_nombres)

repetidos = nombres_primaria.intersection(nombres_secundaria)
print("Nombres que se repiten entre primaria y secundaria:")
print(repetidos)

no_repetidos_primaria = nombres_primaria.difference(nombres_secundaria)
print("Nombres de primaria que no se repiten en secundaria:")
print(no_repetidos_primaria)

#Ejercicio 7
ocurrencias = {}

for _ in range(50):
    string = input("Ingresa un string: ")
    for char in string:
        if char in ocurrencias:
            ocurrencias[char] += 1
        else:
            ocurrencias[char] = 1

print("Cantidad total de ocurrencias de cada carácter:")
for char, count in ocurrencias.items():
    print(f"'{char}': {count}")

#Ejercicio 8

goles = [(3, 1), (4, 2), (5, 1), (6, 2), (7, 3), (8, 1), (9, 4), (10, 5), (2, 3), (6, 7),
         (2, 1), (5, 4), (8, 3), (9, 6), (10, 7), (4, 1), (5, 2), (9, 1), (10, 8), (6, 4)]

equipos = {i: {"triunfos": 0, "empates": 0, "derrotas": 0, "goles_marcados": 0, "goles_recibidos": 0} for i in range(1, 11)}

for partido in goles:
    equipo1, equipo2 = partido
    goles_equipo1, goles_equipo2 = 0, 0
    
    if equipo1 < equipo2:
        goles_equipo1 = 1
        goles_equipo2 = 0
    elif equipo1 > equipo2:
        goles_equipo1 = 0
        goles_equipo2 = 1
    else:
        goles_equipo1 = 0
        goles_equipo2 = 0
    
    equipos[equipo1]["goles_marcados"] += goles_equipo1
    equipos[equipo1]["goles_recibidos"] += goles_equipo2
    equipos[equipo2]["goles_marcados"] += goles_equipo2
    equipos[equipo2]["goles_recibidos"] += goles_equipo1
    
    if goles_equipo1 > goles_equipo2:
        equipos[equipo1]["triunfos"] += 1
        equipos[equipo2]["derrotas"] += 1
    elif goles_equipo1 < goles_equipo2:
        equipos[equipo1]["derrotas"] += 1
        equipos[equipo2]["triunfos"] += 1
    else:
        equipos[equipo1]["empates"] += 1
        equipos[equipo2]["empates"] += 1

for equipo, estadisticas in equipos.items():
    diferencia_de_goles = estadisticas["goles_marcados"] - estadisticas["goles_recibidos"]
    puntos = (estadisticas["triunfos"] * 3) + estadisticas["empates"]
    print(f"Equipo {equipo}: Triunfos = {estadisticas['triunfos']}, Empates = {estadisticas['empates'], Derrotas = {estadisticas['derrotas']}, Diferencia de Goles = {diferencia_de_goles}, Puntos = {puntos}")

#Ejercicio 9


#Ejercicio 10

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_principal = [matriz[i][i] for i in range(len(matriz))]
diagonal_inversa = [matriz[i][len(matriz) - 1 - i] for i in range(len(matriz)]

print("Diagonal Principal:", diagonal_principal)
print("Diagonal Inversa:", diagonal_inversa)


#Ejercicio 11

divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

divisa = input("Ingresa una divisa: ")


if divisa in divisas:
    simbolo = divisas[divisa]
    print(f"El símbolo de {divisa} es: {simbolo}")
else:
    print("La divisa no está en el diccionario.")


#Ejercicio 12

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu número de teléfono: ")

informacion = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}


mensaje = f"{informacion['nombre']} tiene {informacion['edad']} años, vive en {informacion['direccion']} y su número de teléfono es {informacion['telefono']}."
print(mensaje)

#Ejercicio 13

precios_frutas = {
    'manzana': 1.5,
    'banana': 0.75,
    'pera': 1.2,
    'naranja': 0.9,
    'uva': 2.5
}

fruta = input("Ingresa el nombre de la fruta: ").lower()

if fruta in precios_frutas:
    try:
        cantidad_kilos = float(input("Ingresa la cantidad de kilos: "))
        precio_total = precios_frutas[fruta] * cantidad_kilos
        print(f"El precio de {cantidad_kilos} kilos de {fruta} es: {precio_total} euros.")
    except ValueError:
        print("Cantidad no válida. Debe ser un número.")
else:
    print("La fruta ingresada no está en el diccionario de precios.")

