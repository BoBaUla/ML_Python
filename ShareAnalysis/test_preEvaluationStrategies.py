from Evaluation.PreEvaluationStrategies import  *
# pytest test_PreEvaluationStrategies.py


class TestBuyAtLocalMinimum(object):
    
    
    def test_getNextValueAtFirstStep_ReturnsFalse(self):
        data = [5,6,5,5,4,5,5,5,5,4,0,5,6,5,7,5,4,5,5,5,5]
        
        result = buyAtLocalMinimum_Evaluation(data,len(data))
        expectedResult = False

        assert result == expectedResult

    def test_getNextValueAtFirstStep_ReturnsTrue(self):
        data = [5,6,5,5,4,5,5,5,5,4,0,5,6,5,7,5,4,5,5,5,0]
        
        result = buyAtLocalMinimum_Evaluation(data, len(data))
        expectedResult = True

        assert result == expectedResult