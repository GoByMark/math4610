import numpy as np

def L2_Norm (arr1):
    norm = np.linalg.norm(arr1, ord=2)
    return norm