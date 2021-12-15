import numpy as np
from absErr import absErr

exVal = input('Enter the Exact Value:\n')

apprVal = input('Enter the Approximate Value:\n')

absErr(np.float32(exVal), np.float32(apprVal))