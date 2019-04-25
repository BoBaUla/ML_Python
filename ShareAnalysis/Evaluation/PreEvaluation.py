from Helpers.WeightsHelper import ExpectedValue

def preEvaluateDataByRisingExpectedValue(data, steps = 1):
    # print('preEvaluateData')
    if steps == 0:
        return []
    evaluatedData = []
    lastIndex = len(data)- steps + 1
    for i in range(lastIndex-1):
        subset = data[i: i+steps]    

        buy = ExpectedValue(subset,1) < subset[steps - 1]

        subset.append(buy)
        evaluatedData.append(subset)
    return evaluatedData


def preEvaluateDataByFallingExpectedValue(data, steps = 1):
    # print('preEvaluateData')
    if steps == 0:
        return []
    evaluatedData = []
    lastIndex = len(data)- steps + 1
    for i in range(lastIndex-1):
        subset = data[i: i+steps]    

        buy = ExpectedValue(subset,1) > subset[steps - 1]

        subset.append(buy)
        evaluatedData.append(subset)
    return evaluatedData

def EndIntervallEvaluation(data, steps = 1):
    if steps == 0:
        return []
    evaluatedData = []
    lastIndex = len(data)- steps + 1
    for i in range(lastIndex-1):
        subset = data[i: i+steps]    

        buy = subset[0] > subset[steps - 1]

        subset.append(buy)
        evaluatedData.append(subset)
    return evaluatedData

def StartIntervallEvaluation(data, steps = 1):
    if steps == 0:
        return []
    evaluatedData = []
    lastIndex = len(data)- steps + 1
    for i in range(lastIndex-1):
        subset = data[i: i+steps]    

        buy = subset[0] > subset[steps - 1]

        subset.append(buy)
        evaluatedData.append(subset)
    return evaluatedData