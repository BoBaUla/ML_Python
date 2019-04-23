from Helpers.WeightsHelper import ExpectedValue

def preEvaluateData(data, steps = 1):
    # print('preEvaluateData')
    if steps == 0:
        return []
    evaluatedData = []
    lastIndex = len(data)- steps + 1
    for i in range(lastIndex):
        subset = data[i: i+steps]    

        buy = ExpectedValue(subset) < subset[steps - 1]

        subset.append(buy)
        evaluatedData.append(subset)
    return evaluatedData


   