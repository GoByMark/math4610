import numpy as np

def OutPro(arr1, arr2):
    if len(arr1) != len(arr2):
        print('two vectors are not the same length')

    OutPro = np.outer(arr1, arr2)
    return OutPro