import numpy as np
from matAdd import MatAdd
from matSub import MatSub
from matScaMul import MatScaMul
from matTran import MatTran
from matVecPro import MatVecPro
from matMatPro import MatMatPro

# testing matrices, vector, and constant
mat1 = np.array([[2, -7, 5], [-6, 2, 0]])
mat2 = np.array([[5, 8, -5], [3, 6, 9]])
matR = np.array([[5, 1, 3], [1, 1, 1], [1, 2, 1]])
arr = np.array([1, 2, 3])
C = 2

print('Matrix Addition Result:\n', MatAdd(mat1, mat2))
print('Matrix Subtraction Result:\n', MatSub(mat1, mat2))
print('Scalar Multiplication for a Matrix Result:\n', MatScaMul(C, mat1))
print('The Transpose of a Matrix Result:\n', MatTran(mat1))
print('The Product of a Rectangular Matrix and Vector Result:\n', MatVecPro(matR, arr))
print('The Product of Two Rectangular Matrices Result:\n', MatMatPro(matR, matR))