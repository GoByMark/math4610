import numpy as np

def Linf_Norm_Error (arr1, arr2):
    norm = np.linalg.norm((arr1 - arr2), ord=np.inf)
    return norm