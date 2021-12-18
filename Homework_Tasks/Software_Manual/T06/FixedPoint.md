**Routine Name:** sMacEps  

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_06](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_06/Tasksheet%2006.pdf)

Code for sMacEps.cpp:  
```Python
import numpy as np

def f(x):
    return np.exp(-np.power(x, 2)) * np.sin(4 * np.power(x,2) - 1) + 0.051

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return np.exp(-np.power(x, 2)) * np.sin(4 * np.power(x,2) - 1) + 0.051

def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        # print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        if step > N:
            flag = 0
            break
        condition = abs(f(x1)) > e
    if flag == 1:
        print('\nThe root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Input Section
#x0 = float(input('Guess the root: '))
#e = float(input('Tolerable error: '))
#N = int(input('Maximum steps: '))

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
