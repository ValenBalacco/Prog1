#Calcular el perímetro y área de un rectángulo dada su base y su altura. 
base = int(input('Ingrese la base: ')) 
altura = int(input('Ingrese la altura: ')) 
perímetro = base*2+altura*2 
print(perímetro) 
area = base*altura+0 
print(area) 

#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. 

cateto1 = int(input('Ingrese el primer cateto: ')) 

cateto2 = int(input('Ingrese el segundo cateto: ')) 

hipotenusa = (cateto1**2+cateto2 **2)**(1/2) 

print(hipotenusa) 

#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos. 

numero1 = int(input("Ingrese el primer número: "))   

numero2 = int(input("Ingrese el segundo número: "))   

suma = numero1 + numero2   

resta = numero1 - numero2   
division = numero1 / numero2   
multiplicacion = numero1 * numero2  
print("Suma: " + str(suma))   
print("Resta: " + str(resta))   
print("División: " + str(division))   
print("Multiplicación: "+str(multiplicacion)) 
# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: 
farenheit = int(input("Ingrese los grados en Farenheit: "))   
celsius = (farenheit-32)*(5/9) 
print('En grados Celsius es: '+str(celsius)+'°') 
#¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías? 

#A = input(nombre, “¿Cuál es tu canción favorita?”) 
#Al input solo se le puede poner texto entre comillas, el nombre no va ahi. 

nombre = input('¿Cuál es tu canción favorita?') 

#precio = input('Precio: ') 

#total = precio + (precio * 0.1) 

#Falta convertir precio en entero, input lo toma como string. 

precio = int(input('Precio: ')) 

total = precio + (precio * 0.1) 

#​edad = int(input('Edad: ')) 

#print(tu edad es, edad) 

#Falta ponerte comillas al texto en el print 


edad = int(input('Edad: '))  

print("tu edad es", edad) 

#edad = int(input('Edad: ')) 

#print(“Veamos si tu edad es 18…”, edad=18) 

edad = int(input('Edad: '))  

print("Veamos si tu edad es 18…", edad) 

#Calcular la media de tres números pedidos por teclado. 

numero1 = int(input("Ingrese el primer número: ")) 

numero2 = int(input("Ingrese el segundo número: ")) 

numero3 = int(input("Ingrese el tercer número: ")) 
media = (numero1 + numero2 + numero3) / 3 
print("La media de los tres números es:" + str(media)) 
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos. 
minutos = int(input("Ingrese la cantidad de minutos: "))   
hora = minutos//60
minutos= minutos%60   
print("En horas son "+str(hora)+" horas y "+str(minutos)+" minutos") 
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones. 
sueldo_base = int(input("Ingrese su sueldo base: "))  
comisiones = int(input("Ingrese la cantidad de comisiones en el mes: ")) 
comisiones = comisiones*(sueldo_base*0.1) 
sueldo_total = sueldo_base+comisiones  
print("Su sueldo este mes es de: " + str(sueldo_total)) 
#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra. 
precio = int(input("Ingrese el precio del producto: ")) 
precio_descontado = precio-(precio*0.15) 
print("el precio con descuento es de: "+str(precio_descontado)) 
#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes: 
# ​    55% del promedio de sus tres calificaciones parciales. 
# ​    30% de la calificación del examen final. 
# ​    15% de la calificación de un trabajo final. 
parcial1 = int(input("Ingrese la calificación del primer parcial: ")) 
parcial2 = int(input("Ingrese la calificación del segundo parcial: ")) 
parcial3 = int(input("Ingrese la calificación del tercer parcial: ")) 
examen_final = int(input("Ingrese la calificación del examen final: ")) 
trabajo_final = int(input("Ingrese la calificación del trabajo final: ")) 
promedio_parcial = (parcial1 + parcial2 + parcial3) / 3 
calificacion_final = (promedio_parcial * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15) 
print("Su Calificacion total es: "+str(calificacion_final)) 
#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo). 
numero1 = int(input("Ingrese el primer valor: ")) 
numero2 = int(input("Ingrese el segundo valor: ")) 
distancia = abs(numero1 - numero2) 
print("La distancia es de: "+str(distancia)) 
#Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
numero = int(input("Ingrese un número: "))   
raiz2 = numero**(1/2) 
raiz3 = numero**(1/3) 
print("La raíz cuadrada es: "+str(raiz2)) 
print("La raíz cubica es: "+str(raiz3)) 

#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32. 
 
numero = input("Ingrese un numero de 2 cifras: ") 

print("El numero al reves es: "+str(numero[1])+str(numero[0])) 
 
#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables. 

A = int(input("Ingrese el valor de A: ")) 

B = int(input("Ingrese el valor de B: ")) 

cambio = A 

A = B 

B = cambio 

print("Ahora el valor de A es: "+str(A)) 

print("Ahora el valor de B es: "+str(B)) 

#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B. 

HH = int(input("Ingrese la hora de partida: ")) 

MM = int(input("Ingrese los minutos de partida: ")) 

SS = int(input("Ingrese los segundos de partida: ")) 

T = int(input("Ingrese el tiempo de viaje en segundos: ")) 

tiempo_partida = HH * 3600 + MM * 60 + SS 

tiempo_llegada = tiempo_partida + T 

HH2 = tiempo_llegada // 3600 

MM2 = (tiempo_llegada % 3600) // 60 

SS2 = tiempo_llegada % 60 

print("El ciclista llegará a la ciudad B a las " +str(HH2)+":"+str(MM2)+":"+str(SS2)) 

#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales. ​ 

nombre = input("Ingrese su nombre: ") 

apellido1 = input("Ingrese su primer apellido: ") 

apellido2 = input("Ingrese su segundo apellido: ") 

print("Las iniciales son: "+nombre[0]+apellido1[0]+apellido2[0]) 

#Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”. 

usuario = str(input("Ingrese su nombre: "))   

print("Ahora estás en la matrix,"+usuario ) 

#Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar. 

costo = int(input("Ingrese el costo de la cena en el restaurante: ")) 

servicio = costo * 0.062 

propina = costo * 0.1      

monto_total = costo + servicio + propina 

print("El monto total es: "+str(monto_total)) 

#Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa. 

dia = int(input("Ingrese el dia en el que nacio: ")) 

mes = input("Ingrese el mes en el que nacio: ")  

anio = input("Ingrese el año en el que nacio: ")  

print("Su fecha de nacimiento es:" +str(dia)+"/"+str(mes)+"/"+str(anio)) 
#Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA. 

fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato DDMMAAAA: ") 

dia = int(fecha_nacimiento[0:2]) 

mes = int(fecha_nacimiento[2:4]) 

anio = int(fecha_nacimiento[4:]) 

print("Fecha de nacimiento:"+str(dia)+"/"+str(mes)+"/"+str(anio)) 

#Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero. 

#Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán. 

#Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios. 

km_x_litro = int(input("Ingrese cuantos kilometros realiza con 1 litro: "))  
 
litros_x_tanque = int(input("Ingrese cuantos litros almacena su tanque: "))
  
km_recorrido = int(input("Ingrese la cantidad de kilometros en su recorrido: "))  
tanques = (km_recorrido/km_x_litro)/(litros_x_tanque) 

print("En total necesita llenar: " + str(tanques)+" tanques")