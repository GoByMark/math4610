import numpy as np

def f(x):
    return x * np.exp(3*np.power(x, 2)) - 7*x

def secant_Method(x0, x1, e, N):
    print('\n\n*** Secant Method for Root Finding ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x2 = x0 - (x1-x0)*f(x0)/(f(x1) - f(x0))
        x0 = x1 # update the the old x1 to be the new x0
        x1 = x2 # update the the old x2 to be the new x1
        step = step + 1
        if step > N:
            flag = 0
            break
        condition = np.abs(f(x1)) > e
    if flag == 1:
        print('\nThe root is: %0.8f' % x1)
    else:
        print('\nCannot find a root.')

x0 = float(input('Guess the first root: '))
x1 = float(input('Guess the another root: '))
# because of the approximation of the derivative, we need a second guess
e = float(input('Tolerable error: '))
N = int(input('Maximum steps: '))

secant_Method(x0, x1, e, N)