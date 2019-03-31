import scipy as sp 
import numpy as np 
from scipy import stats as st
def mean(list):
    return sp.mean(list)

def median(list):
    return sp.median(list)

def std(list):
    return sp.std(list)

def zScore(list):
    return st.zscore(list)

def grad(list):
    return np.gradient(list)

def relativeChange(list):
    result = []
    for i in range(len(list)-1):
        result.append(list[i+1]/list[i] - 1)
    return result

def logChange(list):
    result = []
    for i in range(len(list)-1):
        result.append(np.log(list[i+1]/list[i]))
    return result

def logChangeInverse(list):
    result = []
    for el in list:
        result.append(np.exp(el))
    return result

list = (1,1,2,2,4,4,5,6)
print(mean(list))
print(median(list))
print(std(list))
print(zScore(list))
print(grad(list))
print(relativeChange(list))
print(logChange(list))
print(logChangeInverse(logChange(list)))