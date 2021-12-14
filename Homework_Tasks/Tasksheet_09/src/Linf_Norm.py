import numpy as np

def Linf_Norm (arr1):
    norm = np.linalg.norm(arr1, ord=np.inf)
    return norm