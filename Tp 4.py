#Ejercicio 1 en Ingles
x = 0

while x <= 30:
    if x == 15:
        print("La ejecución del bucle se interrumpió cuando x era igual a " + str(x) + ".")
        break

    if x == 4 or x == 6 or x == 10:
        print("Se omitió el valor " + str(x) + " de x.")
        x += 1
        continue

    print('El valor del bucle es: ' + str(x))
    x += 1
    
#Ejercicio 1

print("Ingrese líneas (deje una línea en blanco para finalizar):")

while True:
    line = input()
    if line == "":
        break
    print(line.upper())

#Ejercicio 2

balance = 0

while True:
    operation = input("Ingrese una operación (D para depósito, R para retiro, o línea en blanco para finalizar): ")
    
    if operation == "":
        break
    
    if operation == "D":
        amount = float(input("Ingrese el monto a depositar: "))
        balance += amount
    elif operation == "R":
        amount = float(input("Ingrese el monto a retirar: "))
        balance -= amount

print(f"Saldo final: {balance}")

#Ejercicio 3

prime_count = 0

while True:
    number = int(input("Ingrese un número mayor que 1 (0 para finalizar): "))
    
    if number == 0:
        break
    
    if number <= 1:
        continue
    
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_count += 1

print(f"Ha ingresado {prime_count} números primos.")

#Ejercicio 4

start = int(input("Ingrese el año de inicio: "))
end = int(input("Ingrese el año de fin: "))

for year in range(start, end + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if year % 10 == 0:
            print(year)

#Ejercicio 5

for number in range(1, 21):
    if number % 2 != 0:
        continue
    print(number)

#Ejercicio 6

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
number_to_find = int(input("Ingrese un número para buscar: "))

for number in numbers:
    if number == number_to_find:
        print(f"¡Encontrado! {number} está en la lista.")
        break
else:
    print(f"{number_to_find} no está en la lista.")

#Ejercicio 7

while True:
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir")
    
    choice = input("Seleccione una opción (0-3): ")
    
    if choice == "0":
        print("Saliendo del programa.")
        break
    elif choice == "1":
        print("Ha elegido la Opción 1.")
    elif choice == "2":
        print("Ha elegido la Opción 2.")
    elif choice == "3":
        print("Ha elegido la Opción 3.")
    else:
        print("Opción no válida. Seleccione una opción del menú.")
