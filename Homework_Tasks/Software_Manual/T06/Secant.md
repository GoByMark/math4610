**Routine Name:** Secant  

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_06](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_06/Tasksheet%2006.pdf)

Code for Secant.py:  
```Python
import numpy as np

def f(x):
    return np.exp(-np.power(x, 2)) * np.sin(4 * np.power(x,2) - 1) + 0.051

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

#x0 = float(input('Guess the first root: '))
#x1 = float(input('Guess the another root: '))
# because of the approximation of the derivative, we need a second guess
#e = float(input('Tolerable error: '))
#N = int(input('Maximum steps: '))

#secant_Method(x0, x1, e, N)

# x0 = float(input('Guess the root: '))
# e = float(input('Tolerable error: '))
# N = int(input('Maximum steps: '))
```

And the following is the testing code:
```Python
from Newton import newton_Method
from Secant import secant_Method
from FixedPoint import fixedPointIteration
from Bisection import bisection

fixedPointIteration(0.3, 0.0005, 200)

bisection(0.3, 0.7, 200)

newton_Method(0.5, 0.0005, 200)

secant_Method(0.3, 0.7, 0.0005, 200)

```
