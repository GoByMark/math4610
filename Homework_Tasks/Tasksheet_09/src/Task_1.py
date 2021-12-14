import numpy as np
from VecAdd import VecAdd
from VecSub import VecSub
from ScaMul import ScaMul
from DotPro import DotPro
from OutPro import OutPro

# testing vectors and constant
arr1 = np.array([1, 1, 1])
arr2 = np.array([1, 2, 3])
C = 2

print('Vector Addition Result:', VecAdd(arr1, arr2))
print('Vector Subtraction Result:', VecSub(arr1, arr2))
print('Scalar Multiplication Result:', ScaMul(C, arr1))
print('Dot Product Result:', DotPro(arr1, arr2))
print('Outer Product Result:\n', OutPro(arr1, arr2))
