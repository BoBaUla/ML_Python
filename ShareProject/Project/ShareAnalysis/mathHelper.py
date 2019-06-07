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

def returnFromDataRelativ(dataList):
    result = []
    for i in range(len(dataList)-1):
        result.append(returnRelative(dataList[i],dataList[i+1]))
    return result

def returnRelative(value0, value1):
    return (value1-value0)/(value0)

def getBinomialPropability(data, limit = 0):
    n = len(data)
    m = 0
    for value in data:
        if value > limit:
            m = m +1
    if n > 0:
        return m / n
    return 0
    
def getRelationLargerThan(value, dataset):
    length = len(dataset)
    count = 0
    for dat in dataset:
        if dat < value:
            count = count + 1
    return count / length

def linearInterpolation(dataset):
    xValue = range(len(dataset))
    yValue = dataset
    return m.polyfit(xValue, yValue, 1)

def squareInterpolation(dataset):
    xValue = range(len(dataset))
    yValue = dataset
    return m.polyfit(xValue, yValue, 2)    