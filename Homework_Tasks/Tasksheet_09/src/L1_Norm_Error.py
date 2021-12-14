import numpy as np

def L1_Norm_Error (arr1, arr2):
    norm = np.linalg.norm((arr1 - arr2), ord=1)
    return norm