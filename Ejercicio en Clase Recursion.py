#Ejercicio 1

import random

def tiempo_para_escapar():
    tiempo_total = 0
    
    while True:
        camino_elegido = random.randint(1, 3)
        
        if camino_elegido == 1:
            tiempo_total += 3
        elif camino_elegido == 2:
            tiempo_total += 5
        else:
            tiempo_total += 7
            break
        
    return tiempo_total

tiempo_salida = tiempo_para_escapar()
print("La rata tardó", tiempo_salida, "minutos en salir de la jaula.")


#Ejercicio 2  

def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(s[:-1])

