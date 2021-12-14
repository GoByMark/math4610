import numpy as np

def DotPro(arr1, arr2):
    if len(arr1) != len(arr2):
        print('two vectors are not the same length')

    DotPro = np.dot(arr1, arr2)
    return DotPro