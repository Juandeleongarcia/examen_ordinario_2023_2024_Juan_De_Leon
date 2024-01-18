import time
tiempo_carlsen = 180
tiempo_nakamura = 180
tiempo_movimiento = 10
turno = "Carlsen"

def mostrar_estado():
    print(f"\nTiempo restante - Carlsen: {tiempo_carlsen} segundos | Nakamura: {tiempo_nakamura} segundos")
    print(f"Turno: {turno}")

mostrar_estado()

while True:
    movimiento = input(f"Ingrese el jugador que realiza el movimiento ({turno}): ")
    if movimiento != turno:
        print("Error: No es el turno de este jugador. Intenta de nuevo.")
        continue
    if turno == "Carlsen":
        tiempo_carlsen -= tiempo_movimiento
    else:
        tiempo_nakamura -= tiempo_movimiento
    turno = "Nakamura" if turno == "Carlsen" else "Carlsen"
    if tiempo_carlsen <= 60 or tiempo_nakamura <= 60:
        tiempo_movimiento = 5

    mostrar_estado()

    if tiempo_carlsen <= 0 or tiempo_nakamura <= 0:
        print("¡La partida ha finalizado!")
        if tiempo_carlsen < tiempo_nakamura:
            print("¡Magnus Carlsen ha ganado!")
        elif tiempo_nakamura < tiempo_carlsen:
            print("¡Hikaru Nakamura ha ganado!")
        else:
            print("¡La partida ha terminado en empate!")
        break

    salir = input("¿Deseas salir del juego? (Ingrese 'Salir' para terminar): ")
    if salir.lower() == "salir":
        print("¡La partida ha sido interrumpida!")
        break

    time.sleep(1)
