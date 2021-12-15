import numpy as np
from matInfNorm import matInfNorm

# testing matrix
A = [[1, 2, 3], [5, 5, 66], [9, 3, 11]]

print('The Matrix 1-Norm Result(Routine): ', matInfNorm(A))
print('The Matrix 1-Norm Result(Numpy): ', np.linalg.norm(A, ord=np.inf))