import numpy as m

def returnFromData(dataList, stretch = 1):
    result = [0]
    listLen = len(dataList)
    if listLen == 0 | listLen == 1:
        return result
    offset = 1
    for i in range(listLen - 1 - offset):
        result.append(returnInLn(dataList[i], dataList[i+1], stretch))
    return result

def returnInLn(value0, value1, stretch = 1):
    result = m.log(value1/value0)
    return result * stretch

def getBinomialPropability(data, limit = 0):
    n = len(data)
    m = 0
    for value in data:
        if value > limit:
            m = m +1
    if n > 0:
        return m / n
    return 0
    
