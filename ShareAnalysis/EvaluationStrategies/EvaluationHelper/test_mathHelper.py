import mathHelper as mh
import numpy as np

def test_returnInLn_Equal0():
    assert mh.returnInLn(1,1) == 0

def test_returnInLn_Greater0():
    assert mh.returnInLn(1,2) > 0

def test_returnInLn_Smaller0():
    assert mh.returnInLn(2,1) < 0
    
def test_returnFromData_Returns0IfDataListLengthIs0():
    listToTest = []
    result = mh.returnFromData(listToTest)
    assert result == [0]

def test_returnFromData_Returns0IfDataListLengthIs1():
    listToTest = [np.random.rand()]
    result = mh.returnFromData(listToTest)
    assert result == [0]

def test_returnFromData_ReturnsSomethingIfDataListLengthIsGreater1():
    listToTest = [np.random.rand(), np.random.rand(), np.random.rand()]
    result = mh.returnFromData(listToTest)
    assert len(result) == len(listToTest) - 1

def test_getBinomialPropability_WithRespectToLimit1():
    listToTest = [0,1,2,3]
    expectedResult = 0.5
    result = mh.getBinomialPropability(listToTest,1)
    assert expectedResult == result

def test_getBinomialPropability_WithRespectToLimit2():
    listToTest = [0,1,2,3]
    expectedResult = 0.25
    result = mh.getBinomialPropability(listToTest,2)
    assert expectedResult == result