import random

# Lista de palabras
palabras = ["zanahoria", "lechuga", "tomate", "acelga", "berenjena"]

# Función para seleccionar una palabra al azar
def seleccionar_palabra():
    return random.choice(palabras)

# Función para iniciar el tablero
def inicializar_tablero(palabra):
    return ['_' for _ in palabra]

# Función para mostrar el tablero actual
def mostrar_tablero(tablero):
    return ' '.join(tablero)

# Función para jugar el juego del ahorcado
def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    tablero = inicializar_tablero(palabra_secreta)
    intentos_maximos = 6
    intentos = 0
    letras_adivinadas = []

    print("El juego del ahorcado!")
    print("Tienes que adivinar una palabra relacionado con los Vegetales")
    print(mostrar_tablero(tablero))

    while True:
        letra = input("Ingresa una letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in letras_adivinadas:
                print("Ya adivinaste esta letra antes.")
                continue

            letras_adivinadas.append(letra)

            if letra in palabra_secreta:
                print("Adivinaste una letra correctamente.")
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == letra:
                        tablero[i] = letra
            else:
                intentos += 1
                print(f"Letra incorrecta, te quedan {intentos_maximos - intentos} intentos.")

            print(mostrar_tablero(tablero))

            if ''.join(tablero) == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra. ¡Has ganado!")
                break

            if intentos == intentos_maximos:
                print(f"¡Perdiste! La palabra correcta era '{palabra_secreta}'.")
                break
        else:
            print("Ingresa una letra válida.")

if __name__ == "__main__":
    jugar_ahorcado()
