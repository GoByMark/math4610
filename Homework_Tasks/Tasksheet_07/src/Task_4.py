import numpy as np
from matrixD import matrixD

np.set_printoptions(precision=4)

# ask the user for the size of the matrix

n = int(input('Please give the size of this diagonal matrix: '))

# set up the matrix and what not call it inputMatrix?
inputMatrix = matrixD(n)

# to find the solution, probably want to check the determinant first just in case

# initialize the solution and the result vector

x = [1 for i in range(n)]
b = [1 for i in range(n)]

if np.linalg.det(inputMatrix) != 0:
    x = np.dot(np.linalg.inv(inputMatrix), b)
    print("The solution of the given diagonal matrix with result b_i = 1 is, x = ", x)
else:
    print("Please pick a better n next time!")
