laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1],
]
N = 9
PUNTOS_MINIMOS = 23
inicio = (8, 0)
fin = (0, 0)
 
# Orden: arriba, derecha, abajo, izquierda
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
 
 
# Valor de la celda (I y F equivalen a 1; el 0 es pared)
def valor(f, c):
    v = laberinto[f][c]
    return 1 if v == 'I' or v == 'F' else v
 
 
# Puntos que suma la celda: solo los 3 y 4
def puntos_celda(f, c):
    v = laberinto[f][c]
    if v == 3 or v == 4:
        return v
    return 0
 
 
# Comprueba si el raton puede entrar a la celda
def es_valida(f, c, visitado):
    return (
        0 <= f < N
        and 0 <= c < N
        and valor(f, c) != 0
        and not visitado[f][c]
    )
 
 
# Algoritmo de backtracking
def resolver(f, c, visitado, camino, puntos):
    visitado[f][c] = True
    camino.append((f, c))
    puntos += puntos_celda(f, c)
 
    # Comprobar si llego a F con los puntos necesarios
    if (f, c) == fin:
        if puntos >= PUNTOS_MINIMOS:
            return True
    else:
        # Probar los cuatro movimientos
        for df, dc in movimientos:
            nf = f + df
            nc = c + dc
 
            if es_valida(nf, nc, visitado):
                if resolver(nf, nc, visitado, camino, puntos):
                    return True
 
    # Si el camino no funciona, retroceder
    visitado[f][c] = False
    camino.pop()
    return False
 
 
# Mostrar una matriz en pantalla
def mostrar(matriz):
    for fila in matriz:
        print(' '.join(f'{x:>3}' for x in fila))
 
 
print("LABERINTO ORIGINAL")
mostrar(laberinto)
 
visitado = [[False] * N for _ in range(N)]
camino = []
 
if resolver(inicio[0], inicio[1], visitado, camino, 0):
    total = sum(puntos_celda(f, c) for f, c in camino)
    print("\nSe logró salir del laberinto.")
    print("Puntos acumulados:", total)
    print("Movimientos:", len(camino) - 1)
 
    # Crear la matriz solucion
    solucion = []
    for f in range(N):
        fila = []
        for c in range(N):
            if valor(f, c) == 0:
                fila.append('#')
            else:
                fila.append('.')
        solucion.append(fila)
 
    # Numerar las celdas del camino
    for orden, (f, c) in enumerate(camino):
        if (f, c) == inicio:
            solucion[f][c] = 'I'
        elif (f, c) == fin:
            solucion[f][c] = 'F'
        else:
            solucion[f][c] = orden
 
    print("\nMATRIZ SOLUCION")
    print("I = inicio, F = llegada, # = pared")
    mostrar(solucion)
 
    print("\nCamino recorrido:")
    print(camino)
else:
    print("\nNo se logró salir con 23 o más puntos.")
 
    # Mostrar la matriz sin ruta, porque no se encontró camino
    solucion = []
    for f in range(N):
        fila = []
        for c in range(N):
            if valor(f, c) == 0:
                fila.append('#')
            else:
                fila.append('.')
        solucion.append(fila)
    solucion[inicio[0]][inicio[1]] = 'I'
    solucion[fin[0]][fin[1]] = 'F'
 
    print("\nMATRIZ SOLUCION (sin camino)")
    print("I = inicio, F = llegada, # = pared")
    mostrar(solucion)
