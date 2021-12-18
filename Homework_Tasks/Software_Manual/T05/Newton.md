**Routine Name:** Newton  

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_05](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_05/Tasksheet%2005.pdf)

Code for Newton.py:  
```Python
import numpy as np

def f(x):
    return x * np.exp(3*np.power(x, 2)) - 7*x

def df(x):
    return np.exp(3*np.power(x, 2)) + 6 * np.exp(3*np.power(x, 2)) * np.power(x, 2) - 7

def newton_Method(x0, e, N):
    print('\n\n*** Newton Method for Root Finding ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = x0 - f(x0)/df(x0)
        x0 = x1 # update the the old x1 to be the new x0
        step = step + 1
        if step > N:
            flag = 0
            break
        condition = np.abs(f(x1)) > e
    if flag == 1:
        print('\nThe root is: %0.8f' % x1)
    else:
        print('\nCannot find a root.')

x0 = float(input('Guess the root: '))
e = float(input('Tolerable error: '))
N = int(input('Maximum steps: '))

newton_Method(x0, e, N)
```
