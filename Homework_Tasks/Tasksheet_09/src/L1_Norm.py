import numpy as np

def L1_Norm (arr1):
    norm = np.linalg.norm(arr1, ord=1)
    return norm