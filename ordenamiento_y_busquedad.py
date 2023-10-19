# Método de ordenación de burbuja
def ordenacion_burbuja(lista):
    n = len(lista)
    
    for i in range(n):
        intercambio = False
        
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True

        if not intercambio:
            break
    
    return lista

# Método de ordenación por selección
def ordenacion_seleccion(lista):
    n = len(lista)
    
    for i in range(n):
        indice_min = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j

        lista[i], lista[indice_min] = lista[indice_min], lista[i]

    return lista

# Método de ordenación por inserción
def ordenacion_insercion(lista):
    n = len(lista)

    for i in range(1, n):
        clave = lista[i]
        j = i - 1

        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = clave

    return lista

# Método de ordenación fusionada
def ordenacion_fusion(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        ordenacion_fusion(izquierda)
        ordenacion_fusion(derecha)

        indice_izq = indice_der = indice_fusion = 0 

        while indice_izq < len(izquierda) and indice_der < len(derecha):
            if izquierda[indice_izq] < derecha[indice_der]:
                lista[indice_fusion] = izquierda[indice_izq]
                indice_izq += 1
            else:
                lista[indice_fusion] = derecha[indice_der]
                indice_der += 1
            indice_fusion += 1

        while indice_izq < len(izquierda):
            lista[indice_fusion] = izquierda[indice_izq]
            indice_izq += 1
            indice_fusion += 1

        while indice_der < len(derecha):
            lista[indice_fusion] = derecha[indice_der]
            indice_der += 1
            indice_fusion += 1
    
    return lista

# Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista):
        if lista[i] == objetivo:
            return i 
    return -1 

# Búsqueda binaria (funciona con listas ordenadas)
def busqueda_binaria(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1
