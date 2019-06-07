import WeightsHelper as wh


def test_getAllDisjunctElements_Spread0():
    listToTest = [0,0,0.5, 140,1.42,1.2,2]
    disjunctList = [0,140,1,2]

    result = wh.getAllDisjunctElements(listToTest)

    for res in result:
        assert res in disjunctList
    assert len(disjunctList) == len(result)

def test_getAllDisjunctElements_Spread1():
    listToTest = [0,0.51,0.5, 140,1.42,1.2,2]
    disjunctList = [0,0.5, 140,1.4,1.2,2]

    result = wh.getAllDisjunctElements(listToTest, spread =1)

    for res in result:
        assert res in disjunctList
    assert len(disjunctList) == len(result)

def test_getProbability_EqualDistribution():
    # da assert exact prüft, aber bei Berechnungen Rundungsfehler auftreten,
    # muss hier auf eine Umgebung getestet werden.
    delta = 0.00000001
    listToTest = [1,2,3,4,5,6]

    result = wh.getProbability(listToTest, listToTest)
    
    assert sum(result) > 1 - delta
    assert sum(result) < 1 + delta
    for res in result:
        assert res < 1/6 + delta
        assert res > 1/6 - delta

def test_getProbability_UnequalDistribution():
    # da assert exact prüft, aber bei Berechnungen Rundungsfehler auftreten,
    # muss hier auf eine Umgebung getestet werden.
    delta = 0.00000001
    listToTest = [1,1,1,2]
    
    result = wh.getProbability([1,2], listToTest)
    
    assert sum(result) > 1 - delta
    assert sum(result) < 1 + delta
    assert result[0] < 3/4 + delta
    assert result[0] > 3/4 - delta
    assert result[1] < 1/4 + delta
    assert result[1] > 1/4 - delta

def test_generateWeights_EqualDistribution():
    listToTest = [1,2,4,5]
    disjunctElements = [1,2,4,5]
    prop = [1/4, 1/4, 1/4, 1/4]
    expectedResult = (disjunctElements,prop)
    
    result = wh.generateWeights(listToTest)

    assert result == expectedResult

def test_generateWeights_NoEqualDistribution():
    listToTest = [1,2,5,5]
    disjunctElements = [1,2,5]
    prop = [1/4, 1/4, 2/4]
    expectedResult = (disjunctElements,prop)
    
    result = wh.generateWeights(listToTest)

    assert result == expectedResult

def test_generateWeights_NoEqualDistribution_OrderIsCorrect():
    listToTest = [1,1,1,2,2,5]
    disjunctElements = [1,2,5]
    prop = [3/6, 2/6, 1/6]
    expectedResult = (disjunctElements,prop)
    
    result = wh.generateWeights(listToTest)

    assert result == expectedResult

def test_getDataWithRespectToSpread():
    listToTest = [1.21,2.14,3.16]
    expectedResult = [1.2,2.1,3.2]

    result = wh.getDataWithRespectToSpread(listToTest,1)

    assert result == expectedResult

def test_getDataWithRespectToSpread0():
    listToTest = [1.1,2.4,3.6]
    expectedResult = listToTest

    result = wh.getDataWithRespectToSpread(listToTest)

    assert result == expectedResult

def test_ExpectedValue_EqualDistribution():
    # da assert exact prüft, aber bei Berechnungen Rundungsfehler auftreten,
    # muss hier auf eine Umgebung getestet werden.
    delta = 0.00000001
    listToTest = [1,2,3,4,5,6]
    expectedResult = 3.5

    result = wh.ExpectedValue(listToTest)

    assert result > expectedResult - delta
    assert result < expectedResult + delta
