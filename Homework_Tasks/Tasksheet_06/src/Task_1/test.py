from Newton import newton_Method
from Secant import secant_Method
from FixedPoint import fixedPointIteration
from Bisection import bisection

fixedPointIteration(0.3, 0.0005, 200)

bisection(0.3, 0.7, 200)

newton_Method(0.5, 0.0005, 200)

secant_Method(0.3, 0.7, 0.0005, 200)
