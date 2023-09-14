answer = ["Lechuga", "Tomate", "Zanahoria", "Cebolla", "Berenjena"]
clue = 1
level = 1  # Inicializamos el nivel en 1
i = 0

color = ["Verde", "Rojo", "Naranja", "Del Blanco al Amarillento", "Morado"]
inicial = ["L", "T", "Z", "C", "B"]
while level <= 5:  
    print(f"Nivel {level}")
    for mistake in range(3):  # Usamos un bucle for con range para los intentos (mistake)
        while clue <= 3:
            op = input("¿Desea pistas sí o no? Puede solicitar hasta 3 pistas por nivel ").lower()
            if op == "si" or op == "no":
                if op == "no":
                    answer1 = input("Ingrese su respuesta ").title()
                    if answer1 == answer[i]:
                        print(f"Correcto, adivinaste en el intento N{mistake + 1}, la respuesta era {answer[i]}")
                        i += 1
                        clue = 1  
                    else:
                        if mistake == 2:
                            print(f"Perdiste, la respuesta era {answer[i]}")
                        else:
                            print(f"Incorrecto, error N{mistake + 1}")
                        break
                if op == "si":
                    print(f"Pista n°{clue}")
                    if clue == 1:
                        print("Es un vegetal")
                    elif clue == 2:
                        print(f"Es de color {color[i]}")
                    elif clue == 3:
                        print(f"Empieza por {inicial[i]}")
                    clue += 1
            else:
                print("Carácter inválido")
                break
        if clue > 3:
            answer1 = input("Ingrese su respuesta ").title()
            if answer1 == answer[i]:
                print(f"Correcto, adivinaste en el intento N{mistake + 1}, la respuesta era {answer[i]}")
                i += 1
                level += 1
                clue = 1    
            else:
                if mistake == 2:
                    print(f"Perdiste, la respuesta era {answer[i]}")
                else:
                    print(f"Incorrecto, error N{mistake + 1}")