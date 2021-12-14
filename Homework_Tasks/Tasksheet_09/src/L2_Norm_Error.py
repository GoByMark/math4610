import numpy as np

def L2_Norm_Error (arr1, arr2):
    norm = np.linalg.norm((arr1 - arr2), ord=2)
    return norm