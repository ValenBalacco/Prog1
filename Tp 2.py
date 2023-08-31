#Ejercicio 1

anios = int(input("Ingrese la cantidad de años que tiene su computadora: "))

if (anios <= 2):
    print("Su computadora es nueva")

else:

    print("Su computadora es vieja, tiene más de 2 años")   


#Ejercicio 2    

anios = int(input("Ingrese la cantidad de años que tiene su computadora: "))

if (anios <= 2):
    print("Su computadora es nueva")


elif(anios < 0):

    print("Su número ingresado es negativo")


else:

    print("Su computadora es vieja, tiene más de 2 años")   


#Ejercicio 3
 
nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")

if (nombre1[0] == nombre2[0]):

   print("Coincidencia")

else: 

    print("No hay coincidencia")


#Ejercicio 4

respuesta = input("Ingrese uno de los 3 candidatos para votar(A, B, C): ")

respuesta = respuesta.lower()

if(respuesta == 'a'):

    print("Usted ha votado al partido rojo")

elif(respuesta == "b"):

    print("Usted ha votado al partido de la verdad") 

elif(respuesta == "c"):

    print("Usted ha votado al partido azul")
else:
    print("Opción errónea")

#Ejercicio 5    

letra = input("Ingrese una letra: ")


if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
 
     print("Su letra ingresada es una vocal")    
elif(len(letra) > 0):
     
     print("Ingrese una letra, no un String")

#Ejercicio 6

anio = int(input("Ingrese un año: "))

if(anio % 4 == 0 and anio % 100 != 0):

  print("Es un año biciesto")

elif(anio % 100 == 0 and anio % 400 == 0):

  print("Es un año biciesto")

else:

  print("No es un año biciesto")  

#Ejercicio 7

numero1 = int(input("Ingrese el primer número: "))

numero2 = int(input("Ingrese el segundo número: "))

numero3 = int(input("Ingrese el tercer número: "))

menor = numero1

if(menor > numero2):

    menor = numero2

if (menor > numero3):

    menor = numero3

print("El menor es: ", menor )

#Ejercicio 8

nombre = input("Ingrese su nombre: ")
contrasenia = input("Ingrese su contraseña: ")

if (nombre == "Gwenevere" and contrasenia == "excalibur"):

  print("Usuario y contraseña correctos, puede ingresar a Camelot")

else:

  print("Acceso denegado")

#Ejercicio 9

nombre = input("Ingrese la letra de su nombre: ")
sexo = input("Ingrese su sexo: ")
if (sexo == "mujer" and nombre < "m" or sexo == "hombre" and nombre > "n"):
    print("Usted pertenece al grupo A")
else :
    print("Usted pertenece al grupon B")

#Ejercicio 10

edad = int(input("Ingrese la edad del cliente: "))

if(edad < 4):

    print("Puede entrar gratis")

elif(edad >= 4 and edad <= 18):

    print("Usted debe pagar $500")

elif(edad > 18 ):

    print("Usted debe pagar 1000")    

#Ejercicio 11

print("Ingrese una opción")

print("1 - Pizza no Vegana")

print("2 - Pizza Vegana")

opcion = input("Ingrese una de las 2 opciones: 1 / 2: ")

if(opcion == "1"):

    pizza = "No vegana, con "

    print("LISTA DE INGREDIENTES: ")

    print("1- Pepperoni")

    print("2- Jamón")

    print("3- Salmón")

    opcionNV = input("Ingrese un ingrediente 1 / 2 / 3: ")



    if(opcionNV == "1"):

     pizza = pizza + "Pepperoni"

    elif(opcionNV == "2"):

     pizza = pizza + "Jamón"

    elif(opcionNV == "3"):
  
     pizza = pizza + "Salmón"


if(opcion == "2"):

    pizza = "Vegana, con "

    print("LISTA DE INGREDIENTES: ")

    print("1- Tofu")

    print("2- Pimiento" )
   
    opcionV = input("Ingrese un ingrediente 1 / 2: ")
     
    
    if(opcionV == "1"):

     pizza = pizza + "Tofu"

    elif(opcionV == "2"):

     pizza = pizza + "Pimiento"

  


print("Su pizza es", pizza, ", Mozzarella y Tomate")

#Ejercicio 12

anio_actual = int(input("Ingrese el año actual: "))
anio = int(input("Ingrese un año cualquiera: "))

if anio_actual > anio:
    print("Han pasado", anio_actual - anio, " años desde el año ", anio)
elif anio_actual < anio:
    print("Faltan", anio - anio_actual, " años para llegar al año", anio)
else:
    print("Los años son iguales.")

#Ejercicio 13

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 <= 0 or num2 <= 0:
    print("Por favor, ingrese valores positivos y no nulos.")
else:
    if num1 > num2:
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1
        
    if mayor % menor == 0:
        print(mayor, " es múltiplo de ", menor)
    else:
        print(mayor, " no es múltiplo de ", menor)

#Ejercicio 14
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))

if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones.")
    else:
        print("La ecuación no tiene solución.")
else:
    x = -b / a
    print("La solución de la ecuación es x =", x)

#Ejercicio 15
opcion = input("Ingrese 'T' para calcular el área de un triángulo o 'C' para calcular el área de un círculo: ").upper()

if opcion == 'T':
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = 0.5 * base * altura
    print(f"El área del triángulo es ", area)
elif opcion == 'C':
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.14159 * radio ** 2
    print("El área del círculo es ", area)
else:
    print("Opción inválida.")

#Ejercicio 16
a = float(input("Ingrese el primer valor (a): "))
b = float(input("Ingrese el segundo valor (b): "))

print("Operaciones disponibles:")
print("1. Suma")
print("2. Multiplicación")
print("3. Resta")
print("4. División")

opcion = int(input("Ingrese el número de la operación que desea realizar (1/2/3/4): "))

if opcion == 1:
    resultado = a + b
    print("Resultado de ", a, " + ", b, "=", resultado)
elif opcion == 2:
    resultado = a * b
    print("Resultado de ", a, " * ", b, "=", resultado)
elif opcion == 3:
    resultado = a - b
    print("Resultado de ", a, " - ", b, "=", resultado)
elif opcion == 4:
    if b == 0:
        print("No se puede dividir entre cero.")
    else:
        resultado = a / b
        print("Resultado de ", a, " / ", b, "=", resultado)
else:
    print("Opción inválida. Por favor, seleccione una operación válida (1/2/3/4).")

#Ejercicio 17

dia_semana = input("Ingrese un día de la semana: ").lower()

if dia_semana == "lunes":
    print("Es lunes")
elif dia_semana == "viernes":
    print("Es viernes")
elif dia_semana == "sabado" or dia_semana == "domingo":
    print("Es fin de semana")
else:
    print("El día ingresado no es lunes, viernes, sábado ni domingo.")

#Ejercicio 18

horas_trabajadas = int(input("Ingrese el total de horas trabajadas en el mes: "))
salario= float(input("Ingrese el salario por hora: "))

jornada_minima = 48
tarifa_extra = 1.10  # 10% más por horas extras

if horas_trabajadas > jornada_minima:
    horas_extras = horas_trabajadas - jornada_minima
else:
    horas_extras = 0

salario_total = (jornada_minima * salario) + (horas_extras * salario * tarifa_extra)

print(f"Horas extras trabajadas: ", horas_extras)
print(f"Salario total: ", salario_total)

#Ejercicio 19

cantidad_lapices = int(input("Ingrese la cantidad de lápices: "))
costo_por_lapiz = 60  

if cantidad_lapices >= 1000:
    descuento = 0.07  
    costo_total = cantidad_lapices * costo_por_lapiz * (1 - descuento)
else:
    costo_total = cantidad_lapices * costo_por_lapiz

print("El costo total de ", cantidad_lapices, "lápices es: $", costo_total )

#Ejercicio 20
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if promedio >= 6:
    print("El alumno ha aprobado el curso.")
else:
    print("El alumno ha reprobado el curso.")


