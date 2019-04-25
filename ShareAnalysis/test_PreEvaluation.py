from Evaluation.PreEvaluation import preEvaluateData

def test_preEvaluation_Returs0AtNoSteps():
    listToTest = [0]
    expectedResult = []

    result = preEvaluateData(listToTest, 0)

    assert result == expectedResult

def test_preEvaluation_SubsetIsSmallerAsSteps_PerfomNoEvaluation():
    listToTest = [0,2]
    expectedResult = []
    
    result = preEvaluateData(listToTest, 3)

    assert result == expectedResult

def test_preEvaluation_SubsetIsRealSubset_ResultHasCorrectLength():
    listToTest = [0,2,2,3,5,4,2,1]
    steps = 4
    expectedResult = len(listToTest) -  steps
    
    result = preEvaluateData(listToTest, steps)

    assert len(result) == expectedResult

def test_preEvaluation_SubsetIsRealSubset_ResultIsCorrect():
    listToTest = [1,2,3,4,2,1]
    steps = 4
    expectedResult = [[1,2,3,4,True],[2,3,4,2,False]]

    result = preEvaluateData(listToTest, steps)

    assert result == expectedResult