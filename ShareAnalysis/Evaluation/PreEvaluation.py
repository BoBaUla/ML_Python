from Helpers.WeightsHelper import ExpectedValue
from Helpers.mathHelper import linearInterpolation, squareInterpolation

class EvaluatedData():
     def __init__(self, subset, performBuyAction, nextValue):
        self.subset = subset
        self.performBuyAction = performBuyAction
        self.nextValue = nextValue
def lastValue(subset, steps):
    return subset[steps - 1]

def evaluateByFallingSituation(subset, steps):
    return ExpectedValue(subset,1) > lastValue(subset, steps)

def evaluateBuyRisingSituation(subset, steps):
    return ExpectedValue(subset,1) < lastValue(subset, steps)

def endIntervallEvaluation(subset, steps = 1):
    return subset[0] < lastValue(subset, steps)

def startIntervallEvaluation(subset, steps = 1):
    return subset[0] > lastValue(subset, steps)

def linearInterpolationRisingEvaluation(subset, steps = 1):
    return linearInterpolation(subset)[0] > 0

def linearInterpolationFallingEvaluation(subset, steps = 1):
    return linearInterpolation(subset)[0] < 0

def squareInterpolation_HasMinimumEvaluation(subset, steps = 1):
    return squareInterpolation(subset)[0] > 0

def squareInterpolation_HasMaximumEvaluation(subset, steps = 1):
    return squareInterpolation(subset)[0] < 0

def getSubset(data, i, steps):
    return data[i: i+steps]   

def calcLastIndex(data, steps):
    if len(data) < steps:
        return 0

    return len(data)- steps

def getNextValue(currentIndex, steps, data):
    nextIndex = steps + currentIndex
    if nextIndex < len(data):
        return data[nextIndex]
    else:
        return 0

def preEvaluateData(data, steps = 1, evaluation = endIntervallEvaluation):
    # print('preEvaluateData')
    if steps == 0:
        return []
    evaluatedData = []
    lastIndex = calcLastIndex(data, steps)
    for i in range(lastIndex + 1):    # +1 weil die range von 0 bis lastIndex-1 geht
        subset = getSubset(data, i, steps)
        buy = evaluation(subset, steps)
        nextValue = getNextValue(i, steps, data)
        evaluatedData.append(EvaluatedData(subset,buy, nextValue))
    return evaluatedData