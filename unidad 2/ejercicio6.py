mapa = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

fila = int(input("Elige la fila (0 a 4): "))
columna = int(input("Elige la columna (0 a 4): "))

mapa[fila][columna] = "X"

filas = len(mapa)
columnas = len(mapa[0])

for i in range(filas):
    for j in range(columnas):
        print(mapa[i][j], end=" ")
    print()
