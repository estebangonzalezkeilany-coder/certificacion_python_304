# Creando una matriz
numeros = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]

# Obteniendo el número de filas
filas = len(numeros)  # filas = 3

# Obteniendo el número de columnas (contando los elementos de la primera fila)
columnas = len(numeros[0])  # columnas = 3

# Ciclo externo para los índices de las filas
for i in range(filas):
    # Ciclo interno para el índice de las columnas (j)
    for j in range(columnas):
        # Imprime la posición y el valor correspondiente
        print(f"[{i}],[{j}] = {numeros[i][j]}")

