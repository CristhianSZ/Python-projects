import random

dado1 = ["lado1dado1", "lado2dado1", "lado3dado1", "lado4dado1", "lado5dado1", "lado6dado1"]
dado2 = ["lado1dado2", "lado2dado2", "lado3dado2", "lado4dado2", "lado5dado2", "lado6dado2"]


def lanzar_dados():
    return random.choice(dado1), random.choice(dado2)


print("Lista de dado 1:", dado1)
print("Lista de dado 2:", dado2)

modo = input("Selecciona el modo de juego ('alto' o 'bajo'): ")
jugadores = ["Jugador 1", "Jugador 2"]

for turno in range(6):
    for jugador in jugadores:
        input(jugador + ", presiona Enter para lanzar los dados...")
        resultado_dado1, resultado_dado2 = lanzar_dados()
        print("Resultados de los dados (" + jugador + "):", resultado_dado1 + ", " + resultado_dado2)

        suma_resultados = dado1.index(resultado_dado1) + dado2.index(resultado_dado2) + 2

        if turno == 0 or (modo == "alto" and suma_resultados > mejor_suma) or (
                modo == "bajo" and suma_resultados < mejor_suma):
            mejor_suma = suma_resultados
            ganador = jugador

        print("Suma de resultados (" + jugador + "):", suma_resultados)
        print("-" * 30)

    print("Turno " + str(turno + 1) + " finalizado. Ganador del turno: " + ganador + "\n")

print("¡El ganador final es: " + ganador + "!")
