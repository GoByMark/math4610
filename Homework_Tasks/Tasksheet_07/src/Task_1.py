import numpy as np
from matrixU import matrixU

np.set_printoptions(precision=4)

# ask the user for the size of the matrix

n = int(input('Please give the rows of this upper triangular matrix: '))
m = int(input('Please give the columns of this upper triangular matrix: '))

# set up the matrix and what not call it inputMatrix?
inputMatrix = matrixU(n, m)

# to find the solution, probably want to check the determinant first just in case

# initialize the solution and the result vector

x = [1 for i in range(m)]
b = [1 for i in range(n)]

if np.linalg.det(inputMatrix) != 0:
    x = np.matmul(np.linalg.inv(inputMatrix), b)
    print("The solution of the given upper triangular matrix with result b_i = 1 is,\n x =", x)
else:
    print("Please pick a better n and m next time!")
