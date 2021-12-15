import numpy as np

def f(x):
    return x * np.exp(3*np.power(x, 2)) - 7*x

def df(x):
    return np.exp(3*np.power(x, 2)) + 6 * np.exp(3*np.power(x, 2)) * np.power(x, 2) - 7

def hybrid_Method(a, b, x0, e, N):
    print('\n\n*** Hybird Method for Root Finding ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = x0 - f(x0) / df(x0)
        x0 = x1  # update the the old x1 to be the new x0
        step = step + 1
        e1 = np.abs(x1 - x0)  # the error from the Newton method
        while e1 > e:  # the condition needed to start the bisection loop
            a_n = a
            b_n = b
            x0 = m_n  # print("The OG guessed root has become", m_n)
            e2 = np.abs(-f(m_n) / df(m_n))
            if e2 < e:  # check the error to get back to Newton's method
                break
            # recall from the lecture a good rule of thumb for n (bisection) is 4
            for n in range(0, 3):
                m_n = (a_n + b_n) / 2
                if f(a_n) * f(m_n) < 0:
                    a_n = a_n
                    b_n = m_n
                elif f(b_n) * f(m_n) < 0:
                    a_n = m_n
                    b_n = b_n
                elif f(m_n) == 0:
                    print("Found exact solution using Bisection steps:", f(m_n))
        if step > N:
            flag = 0
            break
        condition = np.abs(f(x1)) > e
    if flag == 1:
        print('\nFound solution: %0.8f' % x1)
    else:
        print("We don't have a root in this interval")

a = float(input('Guess the left end point: '))
b = float(input('Guess the right end point: '))
x0 = float(input('Guess the root: '))
e = float(input('Tolerable error: '))
N = int(input('Maximum steps: '))

hybrid_Method(a, b, x0, e, N)
