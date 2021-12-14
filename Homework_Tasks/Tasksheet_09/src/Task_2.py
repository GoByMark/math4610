import numpy as np
from L1_Norm import L1_Norm
from L2_Norm import L2_Norm
from Linf_Norm import Linf_Norm
from L1_Norm_Error import L1_Norm_Error
from L2_Norm_Error import L2_Norm_Error
from Linf_Norm_Error import Linf_Norm_Error

# testing vectors
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 3, 4, 5])

print('L1 Norm Result:', L1_Norm(arr1))
print('L2 Norm Result:', L2_Norm(arr1))
print('L_infinity Norm Result:', Linf_Norm(arr1))
print('L1 Norm Result for Errors:', L1_Norm_Error(arr1, arr2))
print('L2 Norm Result for Errors:', L2_Norm_Error(arr1, arr2))
print('L_infinity Norm Result for Errors:', Linf_Norm_Error(arr1, arr2))
