import random

def tirar_dados(numero_tiros):        #La funcion de arrojar un resultado aleatorio entre 2 valores desde la biblioteca "random"
    resultados = []
    for _ in range(numero_tiros):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados

def obtener_resultados_jugadores(jugadores, numero_tiros):       #Para solicitar el nombre de los jugadores
    resultados_jugadores = []
    for i in range(jugadores):
        nombre = input(f"Ingrese el nombre del jugador {i + 1}: ")
        resultados = tirar_dados(numero_tiros)        #Para que todos los jugadores tengan la misma cantidad de tiradas
        resultados_jugadores.append((nombre, resultados))
    return resultados_jugadores

def imprimir_resultados(resultados_jugadores):
    for nombre, resultados in resultados_jugadores:
        suma_resultados = sum(resultados)
        print(f"El jugador {nombre} obtuvo los siguientes resultados: {resultados}")
        print(f"La suma de los resultados es: {suma_resultados}")

def determinar_ganador(resultados_jugadores):
    max_puntaje = 0
    ganador = ""
    
    for nombre, resultados in resultados_jugadores:
        suma_resultados = sum(resultados)
        if suma_resultados > max_puntaje:
            max_puntaje = suma_resultados
            ganador = nombre
    
    return ganador, max_puntaje

def jugar():        #En esta función se llama a las demas funciones auxiliares en el orden correcto para que funcione el "juego"
    jugadores = int(input("Ingrese el número de jugadores: "))
    numero_tiros = int(input("Ingrese el número de tiros para todos los jugadores: "))
    resultados_jugadores = obtener_resultados_jugadores(jugadores, numero_tiros)
    imprimir_resultados(resultados_jugadores)
    resultados_jugadores.sort(key=lambda x: sum(x[1]), reverse=True)  # Ordenar por puntaje de mayor a menor
    ganador, puntaje_maximo = determinar_ganador(resultados_jugadores)
    print(f"\n¡El ganador es {ganador} con un puntaje de {puntaje_maximo}!")

jugar()
