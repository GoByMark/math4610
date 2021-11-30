import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

def pivot_matrix(A):
    P, L, U = scipy.linalg.lu(A)
    # pprint.pprint(P)
    return P