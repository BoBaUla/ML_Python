import EvaluationHelper.mathHelper as mh 
from numpy import average

def getAllDisjunctElements(data, spread = 0):
    result = []
    for dat in data:
        value = round(dat, spread)
        if value not in result:
            result.append(value)
    return result

def getProbability(element, basedata):
    countTotal = len(basedata)
    prob = []
    for el in element:
        value = basedata.count(el)
        prob.append(value/countTotal)
    return prob

def generateWeights(data, spread = 0):
    disjunctElements = sorted(getAllDisjunctElements(data, spread))
    prop = getProbability(disjunctElements, data)
    return disjunctElements, prop

def ExpectedValue(data, spread = 0):
    disjunctElements, prob = generateWeights(data, spread)
    return average(disjunctElements, weights=prob)