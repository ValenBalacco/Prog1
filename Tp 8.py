#Ejercicio 1
def contar_digitos(n):
    if n < 0:
        n = -n
    num_str = str(n)
    cantidad_digitos = len(num_str)
    return cantidad_digitos

if __name__ == "__main__":
    numero = 12345
    cantidad = contar_digitos(numero)
    print(f"El número {numero} tiene {cantidad} dígitos.")

#Ejercicio 2

import math

def es_potencia_de(n, b):
    if n <= 0 or b <= 0:
        return False
    log_n_base_b = math.log(n, b)
    return log_n_base_b.is_integer()

if __name__ == "__main__":
    n = 8
    b = 2
    if es_potencia_de(n, b):
        print(f"{n} es una potencia de {b}.")
    else:
        print(f"{n} no es una potencia de {b}.")

#Ejercicio 3
def encontrar_posiciones(a, b, start=0):
    posiciones = []

    if b in a:
        index = a.find(b, start)
        if index != -1:
            posiciones.append(index)
            posiciones.extend(encontrar_posiciones(a, b, index + 1))

    return posiciones

if __name__ == "__main__":
    cadena_a = "abracadabraabracadabra"
    subcadena_b = "abra"
    posiciones = encontrar_posiciones(cadena_a, subcadena_b)
    print(f"Posiciones de '{subcadena_b}' en '{cadena_a}': {posiciones}")

#Ejercicio 4
def par(n):
    if n == 0:
        return True
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False
    else:
        return par(n - 1)

if __name__ == "__main__":
    numero = 7
    if impar(numero):
        print(f"{numero} es impar.")
    else:
        print(f"{numero} es par.")
        
#EJercicio 5
def encontrar_maximo(lista):
    if not lista:
        return None

    if len(lista) == 1:
        return lista[0]

    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    max_izquierda = encontrar_maximo(izquierda)
    max_derecha = encontrar_maximo(derecha)

    return max(max_izquierda, max_derecha)

if __name__ == "__main__":
    lista = [12, 45, 62, 73, 8, 92, 54]
    maximo = encontrar_maximo(lista)
    print(f"El máximo elemento de la lista es: {maximo}")

#Ejercicio 6

def replicar(lista, n):
    if n <= 0:
        return []
    if not lista:
        return []
    
    primer_elemento = [lista[0]] * n
    lista_restante = replicar(lista[1:], n)
    
    return primer_elemento + lista_restante

if __name__ == "__main__":
    lista_original = [1, 3, 3, 7]
    n = 2
    lista_replicada = replicar(lista_original, n)
    print(f"Lista replicada: {lista_replicada}")

#EJericio 7

def calcular_sumatoria(n, p):
    if n == 1:
        return p
    else:
        return n * p + calcular_sumatoria(n - 1, p)

if __name__ == "__main":
    n = int(input("Ingrese un número n: "))
    p = int(input("Ingrese un número p: "))
    
    resultado = calcular_sumatoria(n, p)
    
    print(f"El resultado de K({n}, {p}) es: {resultado}")

#Ejericio 8

def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

if __name__ == "__main__":
    fila = 5
    columna = 2
    resultado = pascal(fila, columna)
    print(f"El valor en la fila {fila} y columna {columna} del Triángulo de Pascal es: {resultado}")

#Ejerciio 9

def combinaciones(lista, k, prefijo=""):
    if k == 0:
        print(prefijo)
        return
    for char in lista:
        nueva_prefijo = prefijo + char
        combinaciones(lista, k - 1, nueva_prefijo)

if __name__ == "__main__":
    caracteres = ["A", "B", "C"]
    longitud = 2
    combinaciones(caracteres, longitud)

#Ejercicio 10

def medidas_hoja_A(N):
    if N == 0:
        return (841, 1189)  # Medidas de la hoja A0
    else:
        ancho_anterior, largo_anterior = medidas_hoja_A(N - 1)
        nuevo_ancho = largo_anterior
        nuevo_largo = ancho_anterior / 2
        return (nuevo_ancho, nuevo_largo)

# Ejemplo de uso
if __name__ == "__main__":
    N = 1  
    ancho, largo = medidas_hoja_A(N)
    print(f"Medidas de la hoja A({N}): Ancho = {ancho} mm, Largo = {largo} mm")

