import numpy as np
from mat1Norm import mat1Norm

# testing matrix
A = [[1, 2, 3], [5, 5, 66], [9, 3, 11]]

print('The Matrix 1-Norm Result(Routine): ', mat1Norm(A))
print('The Matrix 1-Norm Result(Numpy): ', np.linalg.norm(A, ord=1))