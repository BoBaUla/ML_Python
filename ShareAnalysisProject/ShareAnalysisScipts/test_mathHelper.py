import helper_Math as mh
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

def test_getRelationLargerThan_ResultIs0():
    listToTest = [1,2,3,4,5]
    expectedResult = 0
    
    result = mh.getRelationLargerThan(0, listToTest)

    assert expectedResult == result

def test_getRelationLargerThan_ResultIs1():
    listToTest = [1,2,3,4,5]
    expectedResult = 1
    
    result = mh.getRelationLargerThan(6, listToTest)

    assert expectedResult == result

def test_getRelationLargerThan_ResultIsBetween0And1():
    listToTest = [1,2,3,4,5]
    expectedResult = 2/5
    
    result = mh.getRelationLargerThan(3, listToTest)

    assert expectedResult == result