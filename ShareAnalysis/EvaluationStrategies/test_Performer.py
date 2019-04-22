from EvaluationStrategies.Performer import performStrategy

money = 10
cost = 2
dataSrc = [1,2,3,4,5,1,5]
steps = 4
limitFactor = 0
stopLossFactor = 0

def sellStrategy(price, sellAt, stopLoss):
    return True

def buyStrategy(buy, canBuy, money, cost, price):
    return canBuy

def test_performStrategy_PerformBuyAction_PerformNoSellAction():
    evaluatedData = [[1,2,3,4,True]]
    result, buyAction, sellAction = performStrategy(money, cost, evaluatedData, dataSrc, steps, sellStrategy=sellStrategy, buyStrategy= buyStrategy)
    assert result == money - cost
    assert len(buyAction) == 1
    assert len(sellAction) == 0
    
def test_performStrategy_PerformBuyAction_PerformSellAction():
    evaluatedData = [[1,2,3,4,True],[2,3,4,5,False]]
    result, buyAction, sellAction = performStrategy(money, cost, evaluatedData, dataSrc, steps, sellStrategy=sellStrategy, buyStrategy= buyStrategy)
    assert result == 2
    assert len(buyAction) == 1
    assert len(sellAction) == 1
