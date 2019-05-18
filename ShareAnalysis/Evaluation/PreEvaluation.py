from Helpers.WeightsHelper import ExpectedValue

def evaluateBuyFallingSituation(subset, steps):
    return ExpectedValue(subset,1) > subset[steps - 1]

def  evaluateBuyRisingSituation(subset, steps):
    return ExpectedValue(subset,1) < subset[steps - 1]

def endIntervallEvaluation(subset, steps = 1):
    return subset[0] > subset[steps - 1]

def startIntervallEvaluation(subset, steps = 1):
    return subset[0] > subset[steps - 1]
    
def preEvaluateData(data, steps = 1, evaluation = evaluateBuyFallingSituation):
    # print('preEvaluateData')
    if steps == 0:
        return []
    evaluatedData = []
    lastIndex = len(data)- steps + 1
    for i in range(lastIndex-1):
        subset = data[i: i+steps]    

        buy = evaluation(subset, steps)

        subset.append(buy)
        evaluatedData.append(subset)
    return evaluatedData


