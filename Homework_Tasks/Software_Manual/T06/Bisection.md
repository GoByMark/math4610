**Routine Name:** sMacEps  

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_06](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_06/Tasksheet%2006.pdf)

Code for sMacEps.cpp:  
```Python
import numpy as np

def f(x):
    return np.exp(-np.power(x, 2)) * np.sin(4 * np.power(x,2) - 1) + 0.051

def bisection(a,b,N):
    print('\n\n*** Bisection Method ***')
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1, N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution:", f_m_n)
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

#a = float(input('Guess the first root: '))
#b = float(input('Guess the second root: '))
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
