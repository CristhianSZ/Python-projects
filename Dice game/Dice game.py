from random import shuffle

dado1 = [("lado1", 1), ("lado2", 2), ("lado3d", 3), ("lado4", 4), ("lado5", 5), ("lado6", 6)]
dado2 = [("lado1", 1), ("lado2", 2), ("lado3d", 3), ("lado4", 4), ("lado5", 5), ("lado6", 6)]


def tirar_dados(dado1, dado2):
    shuffle(dado1)
    shuffle(dado2)
    return dado1[0][1], dado2[0][1]


def elegir_modo():
    modo = input("Elija la condicion de victoria (mayor/menor): ")
    while modo not in ["mayor", "menor"]:
        print("Modo inválido, por favor elija 'mayor' o 'menor'")
        modo = input("Elija el modo de juego (mayor/menor): ")
    return modo


def jugar():
    jugador1 = 0
    jugador2 = 0
    modo = elegir_modo()
    for i in range(6):
        if i == 3:
            print("Condicion de victorio")
            modo = elegir_modo()

        input("Jugador 1, presiona Enter para tirar los dados")
        dado1_jugador1, dado2_jugador1 = tirar_dados(dado1, dado2)
        suma_jugador1 = dado1_jugador1 + dado2_jugador1
        jugador1 += suma_jugador1
        print("Jugador 1: Dados: ", dado1_jugador1, dado2_jugador1, "Resultado: ", suma_jugador1)

        input("Jugador 2, presiona Enter para tirar los dados")
        dado1_jugador2, dado2_jugador2 = tirar_dados(dado1, dado2)
        suma_jugador2 = dado1_jugador2 + dado2_jugador2
        jugador2 += suma_jugador2
        print("Jugador 2: Dados: ", dado1_jugador2, dado2_jugador2, "Resultado: ", suma_jugador2)

        if modo == "mayor":
            if suma_jugador1 > suma_jugador2:
                print("Gana el Jugador 1 el turno ", i + 1)
            elif suma_jugador2 > suma_jugador1:
                print("Gana el Jugador 2 el turno ", i + 1)
            else:
                print("Empate en el turno ", i + 1)
        else:
            if suma_jugador1 < suma_jugador2:
                print("Gana el Jugador 1 el turno ", i + 1)
            elif suma_jugador2 < suma_jugador1:
                print("Gana el Jugador 2 el turno ", i + 1)
            else:
                print("Empate en el turno ", i + 1)

        print("-" * 30)

    if jugador1 > jugador2:
        print("Gana el Jugador 1 con una puntuación de ", jugador1)
    elif jugador2 > jugador1:
        print("Gana el Jugador 2 con una puntuación de ", jugador2)
    else:
        print("Empate con una puntuación de ", jugador1)


jugar()
