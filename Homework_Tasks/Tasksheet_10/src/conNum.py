import numpy as np
from matrixD import matrixD
from newPowerMethodRoutine import newPowerMethod
from newInversePowerRoutine import newInvPowerMethod

n = int(input('Enter dimension of the diagonal dominant matrix: '))
A = matrixD(n)
x = np.ones(n)

def conditionNumber(mat):
    lM = newPowerMethod(mat, n, x)
    lm = newInvPowerMethod(mat, n, x)
    return np.abs(lM)/np.abs((lm))

print('Condition Number(Routine):', conditionNumber(A))
print('Condition Number(Numpy):', np.linalg.cond(A))
