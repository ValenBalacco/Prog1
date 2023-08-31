#Ejercicio 1

corrimiento = int(input("Ingrese la cantidad de lugares a correr las letras: "))

alfabeto = 'abcdefghijklmnñopqrstuvwxyz' 

for n in range(5):
    mensaje = input("Ingrese el mensaje a encriptar: ")
    mensaje_encriptado = ''

    for letra in mensaje:
        if letra.isalpha():
            es_mayuscula = letra.isupper()
            letra = letra.lower()
            indice = alfabeto.index(letra)
            nuevo_indice = (indice + corrimiento) % 27
            nueva_letra = alfabeto[nuevo_indice]
            if es_mayuscula:
                nueva_letra = nueva_letra.upper()
            mensaje_encriptado += nueva_letra
        else:
            mensaje_encriptado += letra

    print("Mensaje encriptado:", mensaje_encriptado)

#Ejercicio 2


pares_total = 0
impares_total = 0

while True:
    numero = int(input("Ingrese un número: "))
    
    if numero == 0:
      print("Total de dígitos pares leídos:", pares_total)
      print("Total de dígitos impares leídos:", impares_total)
      break
    
    pares = 0
    impares = 0
    numero_abs = abs(numero) 
    
    while numero_abs > 0:
        digito = numero_abs % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero_abs //= 10
    
    pares_total += pares
    impares_total += impares
    
    print("Dígitos pares:", pares)
    print("Dígitos impares:", impares)