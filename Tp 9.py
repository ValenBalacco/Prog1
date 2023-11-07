#Ejercicio 1

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad no puede ser un valor negativo.")

    def set_dni(self, dni):
        if len(dni) == 9:
            self.dni = dni
        else:
            print("El DNI debe tener 9 caracteres.")

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def esMayorDeEdad(self):
        return self.edad >= 18

persona1 = Persona("Juan", 25, "123456789")
persona1.mostrar()
print(f"¿Es mayor de edad? {persona1.esMayorDeEdad()}")

#Ejercicio 2

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()}")
        print(f"Cantidad en la cuenta: {self.cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad ingresada debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser mayor que cero.")


persona2 = Persona("María", 30, "987654321")
cuenta1 = Cuenta(persona2, 1000.0)
cuenta1.mostrar()
cuenta1.ingresar(500.0)
cuenta1.retirar(200.0)
cuenta1.mostrar()

#Ejercicio 3

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtener_lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

lado1 = float(input("Ingrese el valor del primer lado del triángulo: "))
lado2 = float(input("Ingrese el valor del segundo lado del triángulo: "))
lado3 = float(input("Ingrese el valor del tercer lado del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)

print(f"El lado más largo es: {triangulo.obtener_lado_mayor()}")
print(f"El triángulo es de tipo: {triangulo.determinar_tipo()}")


#Ejercicio 4

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        contacto = {"nombre": nombre, "telefono": telefono, "email": email}
        self.contactos.append(contacto)
        print(f"Contacto {nombre} añadido a la agenda.")

    def mostrar_lista_de_contactos(self):
        print("Lista de Contactos:")
        for contacto in self.contactos:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
                return
        print(f"Contacto con nombre {nombre} no encontrado.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                contacto['telefono'] = nuevo_telefono
                contacto['email'] = nuevo_email
                print(f"Contacto {nombre} editado.")
                return
        print(f"Contacto con nombre {nombre} no encontrado.")

    def menu(self):
        while True:
            print("\nMenú de Agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Nombre del contacto: ")
                telefono = input("Teléfono del contacto: ")
                email = input("Email del contacto: ")
                self.agregar_contacto(nombre, telefono, email)
            elif opcion == '2':
                self.mostrar_lista_de_contactos()
            elif opcion == '3':
                nombre = input("Nombre del contacto a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == '4':
                nombre = input("Nombre del contacto a editar: ")
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_email = input("Nuevo email: ")
                self.editar_contacto(nombre, nuevo_telefono, nuevo_email)
            elif opcion == '5':
                print("Agenda cerrada.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")


agenda = Agenda()
agenda.menu()
