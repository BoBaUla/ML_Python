from formatter import changeDirection, makeFloatList, prepareData

def test_changeDirection_Int():
    test_list = [1,2,3,4]
    expected_List = [4,3,2,1]
    result = changeDirection(test_list)
    assert expected_List == result

def test_changeDirection_String():
    test_list = ['1','2','3','4']
    expected_List = ['4','3','2','1']
    result = changeDirection(test_list)
    assert expected_List == result

def test_makeFloatList():
    test_list = ['1,3','231,1']
    expected_List = [1.3,231.1]
    result = makeFloatList(test_list)
    assert expected_List == result

def test_prepareData():
    test_list = ['1,3','231,1']
    expected_List = [231.1, 1.3]
    result = prepareData(test_list)
    assert expected_List == result