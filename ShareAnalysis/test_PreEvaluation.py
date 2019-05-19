from Evaluation.PreEvaluation import  preEvaluateData

class TestPreEvaluateData(object):

    def test_Returs0AtNoSteps(self):
        listToTest = [0]
        expectedResult = []

        result = preEvaluateData(listToTest, 0)

        assert result == expectedResult

    def test_SubsetIsSmallerAsSteps_PerfomNoEvaluation(self):
        listToTest = [0,2]
        expectedResult = []
        
        result = preEvaluateData(listToTest, 3)

        assert result == expectedResult

    def test_SubsetIsRealSubset_ResultHasCorrectLength(self):
        listToTest = [0,2,2,3,5,4,2,1]
        steps = 4
        expectedResult = len(listToTest) -  steps
        
        result = preEvaluateData(listToTest, steps)

        assert len(result) == expectedResult

    def test_SubsetIsRealSubset_ResultIsCorrect(self):
        listToTest = [1,2,3,4,2,1]
        steps = 4
        expectedResult = [[1,2,3,4,False],[2,3,4,2,True]]

        result = preEvaluateData(listToTest, steps)

        assert result == expectedResult