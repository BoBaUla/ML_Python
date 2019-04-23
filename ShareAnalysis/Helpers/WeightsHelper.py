import Helpers.mathHelper as mh 
from numpy import average

def getAllDisjunctElements(data, spread = 0):
    result = []
    for dat in data:
        value = round(dat, spread)
        if value not in result:
            result.append(value)
    return result

def getDataWithRespectToSpread(data, spread=0):
    result = []
    for i in range(len(data)):
        data[i] = round(data[i], spread)
    return data

def getProbability(element, basedata):
    countTotal = len(basedata)
    prob = []
    for el in element:
        value = basedata.count(el)
        prob.append(value/countTotal)
    return prob

def generateWeights(data, spread = 0):
    disjunctElements = sorted(getAllDisjunctElements(data, spread))
    dataWithRespectToSpread = getDataWithRespectToSpread(data, spread)
    prop = getProbability(disjunctElements, dataWithRespectToSpread)
    return disjunctElements, prop

def ExpectedValue(data, spread = 0):
    disjunctElements, prob = generateWeights(data, spread)
    return average(disjunctElements, weights=prob)