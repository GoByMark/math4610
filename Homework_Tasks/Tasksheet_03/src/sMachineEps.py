import numpy as py

def sMachineEps():
    one = py.float32(1.0)
    eps = py.float32(1.0)
    for i in range(1, 1000):
        diff = py.float32(one - (one + eps))
        print('{0:<8s}{1:.16f}{2:<12s}{3:.16f}{4:<6s}{5:10f}'.format('Diff =', diff, ' | Eps = ', eps, ' | Counter: ', i))
        if diff == py.float32(0):
            return diff
        eps = py.float32(0.5*eps)