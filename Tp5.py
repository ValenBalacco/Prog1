#Ejercicio 1 
def validar_dni(numero_dni):
    dni_str = str(numero_dni)
    
    if 7 <= len(dni_str) <= 8:
        return True
    else:
        return False

numero_dni1 = 1234567
numero_dni2 = 123456789
print(validar_dni(numero_dni1))
print(validar_dni(numero_dni2))

#Ejercicio 2

def longitud_ultima_palabra(cadena):
    cadena = cadena.strip()
    palabras = cadena.split()
    if len(palabras) > 0:
        return len(palabras[-1])
    else:
        return 0

cadena1 = "  Esto es una prueba  "
cadena2 = "¡Hola, mundo!"
print(longitud_ultima_palabra(cadena1))
print(longitud_ultima_palabra(cadena2))

#Ejercicio 3
def generar_identificador(nombre, apellido, dni):
    nombres = nombre.lower().split()
    primer_nombre = nombres[0]
    apellido_len = len(apellido)
    dni_str = str(dni)[:3]
    identificador = f"{primer_nombre}{apellido_len}{dni_str}"
    return identificador

def obtener_dni_valido():
    while True:
        dni = input("Ingrese el número de DNI (7 u 8 dígitos): ")
        if dni.isdigit() and (len(dni) == 7 or len(dni) == 8):
            return int(dni)
        else:
            print("El número de DNI no es válido. Debe tener 7 u 8 dígitos.")

while True:
    nombre_completo = input("Ingrese el nombre completo del socio (o nombre vacío para salir): ")
    if not nombre_completo:
        break

    dni = obtener_dni_valido()
    partes_nombre = nombre_completo.split()
    nombre = ' '.join(partes_nombre[:-1])
    apellido = partes_nombre[-1]
    identificador = generar_identificador(nombre, apellido, dni)
    print(f"ID -> {identificador}")
  
  
#Ejercicio 4
def es_multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if es_multiplo(num1, num2):
    print(f"{num1} es múltiplo de {num2}.")
elif es_multiplo(num2, num1):
    print(f"{num2} es múltiplo de {num1}.")
else:
    print("Ninguno de los números es múltiplo del otro.")

#Ejercicio 5
def temperatura_media(temp_max, temp_min):
    return (temp_max + temp_min) / 2

def calcular_temperatura_media_para_varios_dias():
    num_dias = int(input("Ingrese el número de días para los cuales desea calcular la temperatura media: "))
    
    for dia in range(1, num_dias + 1):
        temp_max = float(input(f"Ingrese la temperatura máxima para el día {dia}: "))
        temp_min = float(input(f"Ingrese la temperatura mínima para el día {dia}: "))
        
        temp_media = temperatura_media(temp_max, temp_min)
        print(f"La temperatura media para el día {dia} es: {temp_media}°C")

calcular_temperatura_media_para_varios_dias()

#Ejercicio 6 
def agregar_espacio_entre_letras(texto):
    texto_con_espacios = ' '.join(texto)
    return texto_con_espacios

def programa_principal():
    texto = input("Ingrese un texto: ")
    resultado = agregar_espacio_entre_letras(texto)
    print("Texto con espacios adicionales entre letras:")
    print(resultado)

programa_principal()



