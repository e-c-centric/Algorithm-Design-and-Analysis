import time


def GenerateMagicSquares(n):
    matrix = [[0] * n for _ in range(n)]

    magicSquares = []

    generateSquares(matrix, 0, 0, magicSquares)

    return magicSquares


def generateSquares(matrix, row, col, magicSquares):
    if row == len(matrix) and col == 0:
        if isMagicSquare(matrix):
            magicSquares.append([row[:] for row in matrix])
        return

    nextRow, nextCol = (row, col + 1) if col + \
        1 < len(matrix) else (row + 1, 0)

    for num in range(1, len(matrix)**2 + 1):
        if num not in matrix[row]:
            matrix[row][col] = num

            generateSquares(matrix, nextRow, nextCol, magicSquares)

            matrix[row][col] = 0


def isMagicSquare(matrix):
    magicConstant = sum(matrix[0])  # Sum of the first row of matrix

    for row in matrix:
        if sum(row) != magicConstant:
            return False

    for col in range(len(matrix)):
        if sum(row[col] for row in matrix) != magicConstant:
            return False

    if sum(matrix[i][i] for i in range(len(matrix))) != magicConstant:
        return False

    if sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))) != magicConstant:
        return False

    return True


start_time = time.time()
n = 1
while time.time() - start_time < 60:
    magic_squares = GenerateMagicSquares(n)
    #print(f"Magic squares of order {n}: {len(magic_squares)}")
    n += 1
print(n)