#Ejercicio 1

word = input("Ingrese una palabra: ")

for k in range(10):

 print(word)

#Ejercicio 2

age = int(input("Ingrese su edad: "))

for i in range(age):

    print(i + 1)

#Ejercicio 3

num = int(input("Ingrese un número entero positivo: "))

for i in range(num):

 if (i % 2 != 0):
  
  print(i, end= ", " )

#Ejercicio 4

num = int(input("Ingrese un número positivo: "))

for i in range(num, -1, -1):

 print(i, end=", ")

#Ejercicio 5

inv = int(input("Ingrese la cantidad que inversinó: "))

anual_interest = int(input("Ingrese su interés anual en $: "))

years = int(input("Ingrese la cantidad de años que durará la inversión: "))

for i in range(years):

    inv = inv + anual_interest;

    print("Su inversión generó: ", anual_interest )

    print("---------------------------")

print("El dinero total que recaudó con esa inversión fue de: ", inv)

#Ejercicio 6

num= int(input("Ingrese un número entero: "))

for i in range(1, num + 1):
        
  print('*' * i)

#Ejercicio 7

print("TABLAS DE MULTIPLICAR: ")

for i in range(11):
 
   for j in range(11):
  
    print(i, " x ", j ," = ", i*j)


   print("--------------")

#Ejercicio 8

num = int(input("Ingrese un número entero: "))

num_impares = num if num % 2 != 0 else num - 1

for i in range(num_impares, 0, -2):
 
 for j in range(i, num_impares + 1, 2):
     
     print(j, end=" ")
     
 print()

 #Ejercicio 9

 
password = input("Ingrese una contraseña, esta se guardara y tendra que ingresarla después: ")
salir = False

while salir == False:

 tried = input("Ingrese su contraseña: ")

 if(tried != password):
  
  print("Su contraseña es incorrecta, intentalo nuevamente")

  if(tried == password):
   
   salir = True

#Ejercicio 10
num = int(input("Ingrese un número entero: "))
i = 1
cont = 0
for i in range(1, num):
    
    div = num % i
    i = i + 1 
    if div == 0:
        cont = cont+1
if cont >2:
    print("no es primo")
elif cont<2:
        print("es primo")


#Ejercicio 11
word = input("Ingrese una palabra: ")
for term in reversed(word):
    print(term)

#EJercicio 12
word = input("Ingrese una frase: ").lower()
letter = input("Ingrese una letra: ").lower()
cont = 0

for char in word:
    if char == letter:
        cont += 1

print(f"La letra '{letter}' aparece {cont} veces en la frase.")

#Ejercicio 13
while True:
    inp = input("Ingrese algo (o escriba 'salir' para terminar): ")
    if inp.lower() == "salir":
        break
    print(inp)

#Ejercicio 14
number1 = int(input("Ingrese el primer número entero: "))
number2 = int(input("Ingrese el segundo número entero: "))

for number in range(number1, number2 + 1):
    if number % 2 == 0:
        print(f"{number} es par.")
    else:
        print(f"{number} es impar.")

#Ejercicio 15
number = int(input("Ingrese un número entero mayor que cero: "))
div = []

for i in range(1, number + 1):
    if number % i == 0:
        div.append(i)

print(f"Los divisores de {number} son: {div}")


#Ejercicio 16

num = int(input("¿Cuántos números va a introducir? "))
negative_cont = 0

for i in range(num):
    number = int(input("Ingrese un número: "))
    if number < 0:
        negative_cont += 1

print(f"Ha introducido {negative_cont} números negativos.")

#Ejercicio 17

word = input("Ingrese una frase: ")
vocal = set("aeiouAEIOU")
vocal_in_word = []

for letra in word:
    if letra in vocal:
        if letra not in vocal_in_word:
            vocal_in_word.append(letra)

print("Vocales en la frase:", ", ".join(vocal_in_word))

#Ejercicio 18

a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

#Ejercicio 19

objetivo = float(input("¿Cuánto dinero desea ahorrar? "))
ahorro_total = 0

while ahorro_total < objetivo:
    cantidad = float(input("Ingrese la cantidad que desea ahorrar: "))
    if cantidad < 0:
        print("La cantidad ingresada debe ser positiva.")
        continue
    ahorro_total += cantidad

print(f"¡Felicidades! Ha alcanzado su objetivo de ahorro de ${objetivo}.")

#Ejercicio 20

suma = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print(f"La suma de los números ingresados es: {suma}")

#Ejercicio 21

mayor = 0

while True:
    numero = int(input("Ingrese un número entero positivo (0 para terminar): "))
    if numero == 0:
        break
    if numero > mayor:
        mayor = numero

print(f"El mayor número ingresado es: {mayor}")

#Ejercicio 22

contador_pares = 0

while True:
    numero = int(input("Ingrese un número entero positivo (-1 para terminar): "))
    if numero == -1:
        break
    suma_digitos = sum(int(digit) for digit in str(numero))
    print(f"La suma de los dígitos de {numero} es {suma_digitos}")
    if suma_digitos % 2 == 0:
        contador_pares += 1

print(f"De los números ingresados, {contador_pares} son pares.")

#Ejercicio 23

total = 0

while True:
    amount = float(input("Ingrese el monto de la compra (0 para finalizar): "))
    
    if amount == 0:
        break
    
    if amount < 0:
        print("El monto no puede ser negativo. Ingrese un monto válido.")
        continue
    
    total += amount

print(f"El total de las compras del cliente es: ${total}")


#Ejercicio 24

total = 0

while True:
    amount = float(input("Ingrese el monto de la compra (0 para finalizar): "))
    
    if amount == 0:
        break
    
    if amount < 0:
        print("El monto no puede ser negativo. Ingrese un monto válido.")
        continue
    
    total += amount

if total > 1000:
    discont = total * 0.10
    total -= discont

print(f"El total a pagar es: ${total}")



#Ejercicio 25

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")

