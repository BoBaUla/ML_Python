from PreEvaluation import preEvaluateData

def test_preEvaluation_Returs0AtNoSteps():
    listToTest = [0]
    expectedResult = 0

    result = preEvaluateData(listToTest, 0)

    assert result == expectedResult