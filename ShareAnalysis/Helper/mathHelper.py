import numpy as m
from scipy import stats

def returnInLn(value0, value1, stretch = 1):
    result = m.log(value1/value0)
    return result * stretch

def returnFromData(dataList, stretch = 1):
    result = [0]
    listLen = len(dataList)
    if listLen == 0 | listLen == 1:
        return result
    offset = 1
    for i in range(listLen - 1 - offset):
        result.append(returnInLn(dataList[i], dataList[i+1], stretch))
    return result

def kolelationData(data):
    values = [[],[]]
    for i in range(len(data)-1):
        values[0].append(data[i])
        values[1].append(data[i+1])

    return [zTraf(values[0]), zTraf(values[1])]

def zTraf(data):
   return stats.zscore(data)

def korelationKoefficient(data):
    return stats.pearsonr(data[0], data[1])

def getPropability(data, limit = 0):
    n = len(data)
    m = 0
    for value in data:
        if value > limit:
            m = m +1
    if n > 0:
        return m / n
    return 0
    