import time

def GenerateMagicSquare(n):
    if n % 2 == 1:
        return SiameseMethod(n)
    else:
        return SquareOfSquaresMethod(n)

def SiameseMethod(n):
    matrix = [[0] * n for _ in range(n)]
    
    row = 0
    col = n // 2

    for num in range(1, n*n + 1):
        matrix[row][col] = num
        nextRow = (row - 1 + n) % n
        nextCol = (col + 1) % n
        if matrix[nextRow][nextCol] != 0:
            nextRow = (row + 1) % n
            nextCol = col
        # Update the current position
        row = nextRow
        col = nextCol

    return matrix

def SquareOfSquaresMethod(n):
    matrix = [[0] * n for _ in range(n)]

    subSize = n // 4

    subMatrix1 = GenerateSubSquare(subSize)
    subMatrix2 = GenerateSubSquare(subSize)
    subMatrix3 = GenerateSubSquare(subSize)
    subMatrix4 = GenerateSubSquare(subSize)

    for i in range(subSize):
        for j in range(subSize):
            matrix[i][j] = subMatrix1[i][j]
            matrix[i][j + subSize*2] = subMatrix2[i][j]
            matrix[i + subSize*2][j] = subMatrix3[i][j]
            matrix[i + subSize*2][j + subSize*2] = subMatrix4[i][j]

    return matrix

def GenerateSubSquare(subSize):
    subMatrix = [[0] * subSize for _ in range(subSize)]
    num = 1
    for i in range(subSize):
        for j in range(subSize):
            subMatrix[i][j] = num
            num = num + 1
    return subMatrix

start_time = time.time()
n = 1
while time.time() - start_time < 60:
    magic_square = GenerateMagicSquare(n)
    n += 1
print(n)