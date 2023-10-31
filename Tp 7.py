#Ejercicio 1

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        intercambio_realizado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio_realizado = True
        if not intercambio_realizado:
            break

if __name__ == "__main__":
    lista_numeros = [64, 34, 25, 12, 22, 11, 90]
    ordenamiento_burbuja(lista_numeros)
    print("Lista ordenada:")
    print(lista_numeros)

#Ejercicio 2

def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

if __name__ == "__main__":
    lista_palabras = ["manzana", "banana", "pera", "uva", "naranja"]
    ordenamiento_seleccion(lista_palabras)
    print("Lista ordenada alfabéticamente:")
    print(lista_palabras)

#Ejercicio 3

lista_libros = [
    {"titulo": "Libro A", "autor": "Autor X", "año_publicacion": 2000},
    {"titulo": "Libro B", "autor": "Autor Y", "año_publicacion": 1995},
    {"titulo": "Libro C", "autor": "Autor Z", "año_publicacion": 2010},
    {"titulo": "Libro D", "autor": "Autor X", "año_publicacion": 2005},
]

def ordenar_libros_por_campo(libros, campo):
    return sorted(libros, key=lambda x: x[campo])

libros_ordenados_por_anio = ordenar_libros_por_campo(lista_libros, "año_publicacion")

for libro in libros_ordenados_por_anio:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año de Publicación: {libro['año_publicacion']}")

#Ejercicio 4

def ordenamiento_insercion_por_longitud(lista):
    for i in range(1, len(lista)):
        cadena_actual = lista[i]
        j = i - 1
        while j >= 0 and len(cadena_actual) < len(lista[j]):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = cadena_actual

if __name__ == "__main__":
    lista_cadenas = ["manzana", "banana", "pera", "uva", "naranja"]
    ordenamiento_insercion_por_longitud(lista_cadenas)
    print("Lista ordenada por longitud:")
    print(lista_cadenas)
    
#Ejercicio 5

def ordenamiento_burbuja_descendente(lista):
    n = len(lista)
    for i in range(n):
        intercambio_realizado = False
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio_realizado = True
        if not intercambio_realizado:
            break


if __name__ == "__main__":
    lista_numeros = [64, 34, 25, 12, 22, 11, 90]
    ordenamiento_burbuja_descendente(lista_numeros)
    print("Lista ordenada en orden descendente:")
    print(lista_numeros)
    
    
#Ejercicio 6

def ordenamiento_por_conteo(lista):
    max_valor = max(lista)
    min_valor = min(lista)
    conteo = [0] * (max_valor - min_valor + 1)
    for num in lista:
        conteo[num - min_valor] += 1
    lista_ordenada = []
    for i in range(len(conteo)):
        while conteo[i] > 0:
            lista_ordenada.append(i + min_valor)
            conteo[i] -= 1
    return lista_ordenada

if __name__ == "__main__":
    lista_numeros = [4, 2, 2, 8, 3, 3, 1]
    lista_ordenada = ordenamiento_por_conteo(lista_numeros)
    print("Lista ordenada por conteo:")
    print(lista_ordenada)

#Ejercicio 7

lista_mixta = [3, "manzana", 1, "banana", 4, "pera", "uva", 2, "naranja"]

numeros = [x for x in lista_mixta if isinstance(x, int)]
cadenas = [x for x in lista_mixta if isinstance(x, str)]

numeros.sort()
cadenas.sort()

lista_ordenada = numeros + cadenas

print("Lista ordenada:")
print(lista_ordenada)

#EJercicio 8

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

if __name__ == "__main__":
    lista_numeros = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(lista_numeros)
    print("Lista ordenada:")
    print(lista_numeros)


