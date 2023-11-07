class Motocicleta:

    es_nueva = True
    precio = 0

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.motor = False 

    def arrancar(self):
        if not self.motor:
            self.motor = True
            print("El motor ha arrancado.")
        else:
            print("El motor ya estaba en marcha.")

    def detener(self):
        if self.motor:
            self.motor = False
            print("El motor se ha detenido.")
        else:
            print("El motor ya estaba detenido.")

    def consultar_precio(self):
        return Motocicleta.precio


moto1 = Motocicleta("Rojo", "ABC123", 10, 2, "Honda", "CBR500R", "2023", 180, 190)
moto2 = Motocicleta("Negro", "XYZ789", 8, 2, "Yamaha", "YZF-R6", "2022", 175, 170)


moto1.precio = 5000


moto1.arrancar()
moto1.arrancar()
moto1.detener()
moto1.detener()
moto2.arrancar()
moto2.detener()


print(f"El precio de la motocicleta '{moto1.marca} {moto1.modelo}' es de {moto1.precio} $.")
print(f"El precio de la motocicleta '{moto2.marca} {moto2.modelo}' es de {moto2.consultar_precio()} $.")
