import numpy as np

def absErr(exVal, apprVal):
    absErr = np.abs(exVal - apprVal)
    print('The Approximate Value: ', apprVal)
    print('The Exact Value: ', exVal)
    print('The Absolute Error: ', absErr)
