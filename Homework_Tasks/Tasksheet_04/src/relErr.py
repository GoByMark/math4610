import numpy as np

def relErr(exVal, apprVal):
    relErr = (np.abs(exVal - apprVal))/exVal
    print('The Approximate Value: ', apprVal)
    print('The Exact Value: ', exVal)
    print('The Absolute Error: ', relErr)
