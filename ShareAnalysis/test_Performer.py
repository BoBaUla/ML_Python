import Evaluation.Performer as performer
from Helpers.Config import SimConfig

config = SimConfig(invest=10, fee=2, steps=4, sellAtFactor=0, stopLossFactor=0)
dataSrc = [1,2,3,4,5,1,5]

def sellStrategy(price, sellAt, stopLoss):
    return True

def buyStrategy(buy, canBuy, money, cost, price):
    return canBuy

def test_performStrategy_PerformBuyAction_PerformNoSellAction():
    evaluatedData = [[1,2,3,4,True]]
    result, buyAction, sellAction = performer.performStrategy(config, evaluatedData, dataSrc)
    assert result == config.invest - config.fee
    assert len(buyAction) == 1
    assert len(sellAction) == 0
    
def test_performStrategy_PerformBuyAction_PerformSellAction():
    evaluatedData = [[1,2,3,4,True],[2,3,4,5,False]]
    result, buyAction, sellAction = performer.performStrategy(config, evaluatedData, dataSrc)
    assert result == 2
    assert len(buyAction) == 1
    assert len(sellAction) == 1
