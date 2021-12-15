import numpy as np
from relErr import relErr

exVal = input('Enter the Exact Value:\n')

apprVal = input('Enter the Approximate Value:\n')

relErr(np.float32(exVal), np.float32(apprVal))
