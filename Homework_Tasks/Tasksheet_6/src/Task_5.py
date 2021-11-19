import numpy as np
from matrixS import matrixS

np.set_printoptions(precision=4)

# ask the user for the size of the matrix

n = int(input('Please give the size of this square matrix: '))

# set up the matrix and what not call it inputMatrix?
inputMatrix = matrixS(n)

# to find the reduced row echelon form of inputMatrix without testing bad pivots, we can just do the following

for k in range(n):
    if inputMatrix[k][k] == 0:
        exit('Division by zero detected!')

    for i in range(n):
        if i != k:
            ratio = inputMatrix[i][k] / inputMatrix[k][k]

            for j in range(n):
                inputMatrix[i][j] = inputMatrix[i][j] - ratio * inputMatrix[k][j]

print("The row echelon form of the given square matrix is \n", inputMatrix)