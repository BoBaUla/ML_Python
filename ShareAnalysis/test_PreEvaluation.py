from Evaluation.PreEvaluation import  *
# pytest test_PreEvaluation.py

def evaluationMockMethodTrue(arg1,arg2):
    return True

class TestCalcLastIndex(object):
    data = [0,1,2,3,4]

    def test_Returns0(self):
        val = [0]
        result = calcLastIndex(val, 2)
        assert result == 0

    def test_ReturnsCorrectAmount(self):
        result = calcLastIndex(self.data, 2)
        assert result == 3

class TestGetNextValue(object):
    data = [0,1,2,3,4,5,6]
    steps = 2
    lastIndex = calcLastIndex(data, steps)
     
    def test_getNextValueAtFirstStep(self):
        result = getNextValue(0,self.steps,self.data)
        expectedResult = self.data[self.steps]

        assert result == expectedResult

    def test_getNextValueAtSecondStep(self):
        result = getNextValue(1,self.steps,self.data)
        expectedResult = self.data[self.steps + 1]

        assert result == expectedResult

    def test_getNextValueAtLastStep(self):
       
        result = getNextValue(self.lastIndex,self.steps,self.data)
        expectedResult = 0
        
        assert result == expectedResult

    def test_getNextValueAtPreLastStep(self):
        result = getNextValue(self.lastIndex - 1,self.steps,self.data)
        expectedResult = 6
        
        assert result == expectedResult

class TestGetSubset(object):

    def test_GetSingleSubset(self):
        data = [0,1,2,3,4,5,6,7]
        result = getSubset(data, 0, 3)
        expectedResult = [0,1,2]

        assert result == expectedResult

class TestPreEvaluateData_CuttingSubsets(object):

    data = [0,1,2]

    def test_GetsCorrectSubsets_AtSteps1(self):
        result = preEvaluateData(self.data)
        
        expectedResult = [EvaluatedData([0],[],0), EvaluatedData([1],[],0), EvaluatedData([2],[],0)]

        for i in range(len(expectedResult)):
            assert result[i].subset == expectedResult[i].subset
    
    def test_GetsCorrectSubsets_AtSteps2(self):
        result = preEvaluateData(self.data,2)
        
        expectedResult = [EvaluatedData([0,1],[],0), EvaluatedData([1,2],[],0)]
        
        for i in range(len(expectedResult)):
            assert result[i].subset == expectedResult[i].subset
    
    def test_GetsCorrectSubsets_AtSteps3(self):
        result = preEvaluateData(self.data,3)
        
        expectedResult = [EvaluatedData([0,1,2],[],0)]
        
        for i in range(len(expectedResult)):
            assert result[i].subset == expectedResult[i].subset

class TestPreEvaluationData_SettingNextValue(object):
    
    data = [0,1,2]

    def test_GetsCorrectNext_AtSteps1(self):
        result = preEvaluateData(self.data)
        
        expectedResult = [EvaluatedData([0],[],1), EvaluatedData([1],[],2), EvaluatedData([2],[],0)]

        for i in range(len(expectedResult)):
            assert result[i].nextValue == expectedResult[i].nextValue
    
    def test_GetsCorrectNext_AtSteps2(self):
        result = preEvaluateData(self.data,2)
        
        expectedResult = [EvaluatedData([0,1],[],2), EvaluatedData([1,2],[],0)]
        
        for i in range(len(expectedResult)):
            assert result[i].nextValue == expectedResult[i].nextValue
    
    def test_GetsCorrectNext_AtSteps3(self):
        result = preEvaluateData(self.data,3)
        
        expectedResult = [EvaluatedData([0,1,2],[],0)]
        
        for i in range(len(expectedResult)):
            assert result[i].nextValue == expectedResult[i].nextValue

class TestPreEvaluation_Misc(object):
    
    def test_Returs0AtNoSteps(self):
        listToTest = [0]
        expectedResult = []

        result = preEvaluateData(listToTest, 0)

        assert result == expectedResult

    def test_SubsetIsRealSubset_ResultHasCorrectLength(self):
        listToTest = [0,2,2,3,5,4,2,1]
        steps = 2
        expectedResult = calcLastIndex(listToTest, steps) + 1
        
        result = preEvaluateData(listToTest, steps)

        assert len(result) == expectedResult

    def test_SubsetIsRealSubset_ResultIsCorrect_MockedTrue(self):
        listToTest = [1,2,3,4,2,1]
        steps = 4
        expectedResult = [
            EvaluatedData([1,2,3,4], True, 2),
            EvaluatedData([2,3,4,2], True, 1),
            EvaluatedData([3,4,2,1], True, 0)
            ]


        result = preEvaluateData(listToTest, steps, evaluationMockMethodTrue)

        for i in range(len(expectedResult)):
            assert result[i].nextValue == expectedResult[i].nextValue
            assert result[i].subset == expectedResult[i].subset
            assert result[i].performBuyAction == expectedResult[i].performBuyAction