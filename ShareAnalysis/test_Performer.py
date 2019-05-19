import Evaluation.Performer as performer
from Evaluation.PreEvaluation import *
from Helpers.Config import SimConfig

# pytest test_Performer.py

config = SimConfig(invest=10, fee=2, steps=4, sellAtFactor=0, stopLossFactor=0)
dataSet = EvaluatedData([0,0,0], True, 0)

def sellMockTrue(arg1, arg2, arg3): 
        return True

def sellMockFalse(arg1, arg2, arg3): 
        return False

class TestEnoughMoneyLeft(object):

    def test_ReturnsTrue(self):
        result = performer.enoughMoneyLeft(10,1,1)
        assert result 

    def test_ReturnsFalse(self):
        result = performer.enoughMoneyLeft(10,1,11)
        assert not result 

class TestAdjustMoneyAfterBuyAction(object):
    
    def test_CalcRight(self):
        result = performer.adjustMoneyAfterBuyAction(10, 1, 2, 2)
        assert result == 5

class TestBuyShare(object):
    
    def test_CalcRight(self):
        result = performer.buyShare(10, 1, 3, 2)
        assert result == 5

class TestPerformStrategy(object):
    
    def test_ReturnIfMaxGainIsReached(self):
        config.maxGainFactor = 0
        preEvaluatedData =  [dataSet, dataSet, dataSet]
        result = performer.performStrategy(config,preEvaluatedData)

        expectedResult = (config.invest, [], [])
        assert result == expectedResult
        
    def test_PerformOneBuyAction_PerformNoSellAction(self):
        config.maxGainFactor = 10
        evaluatedData = [
            EvaluatedData([1,2,3,4],True,2), 
            EvaluatedData([1,2,3,4],True,2)]
        gain, buyAction, sellAction = performer.performStrategy(config, evaluatedData, sellStrategy = sellMockFalse)
        assert len(buyAction) == 1
        assert len(sellAction) == 0
    
    def test_PerformOneBuyAction_PerformOneSellAction(self):
        config.maxGainFactor = 1
        evaluatedData = [
            EvaluatedData([1,2,3,4],True,2), 
            EvaluatedData([2,3,4,2],False,10), 
            EvaluatedData([2,3,4,2],False,1), 
            EvaluatedData([2,3,4,2],False,1)]
        gain, buyAction, sellAction = performer.performStrategy(config, evaluatedData, sellStrategy = sellMockTrue)
        assert len(buyAction) == 1
        assert len(sellAction) == 1

    def test_PerformOneBuyAction_PerformOneSellAction_AndMaxGainHits(self):
        config.maxGainFactor = 10
        evaluatedData = [
            EvaluatedData([1,2,3,4],True,2), 
            EvaluatedData([2,3,4,2],False,100), 
            EvaluatedData([2,3,4,2],True,1), 
            EvaluatedData([2,3,4,2],False,1),
            EvaluatedData([2,3,4,2],False,1),
            EvaluatedData([2,3,4,2],True,1)]
        gain, buyAction, sellAction = performer.performStrategy(config, evaluatedData, sellStrategy = sellMockTrue)
        assert gain >= config.invest * (1+config.maxGainFactor)
        assert len(buyAction) == 1
        assert len(sellAction) == 1
    
    def test_PerformOneBuyAction_PerformOneSellAction_IndicesAreSetCorrectly(self):
        config.maxGainFactor = 10
        evaluatedData = [
            EvaluatedData([1,2,3,4],True,2), 
            EvaluatedData([2,3,4,2],False,100), 
            EvaluatedData([2,3,4,2],True,1), 
            EvaluatedData([2,3,4,2],False,1),
            EvaluatedData([2,3,4,2],False,1),
            EvaluatedData([2,3,4,2],True,1)]
        gain, buyAction, sellAction = performer.performStrategy(config, evaluatedData, sellStrategy = sellMockTrue)
        assert len(buyAction) == 1
        assert buyAction[0][0] == len(evaluatedData[0].subset)
        assert len(sellAction) == 1
        assert sellAction[0][0] == len(evaluatedData[0].subset) + 1
      
    def test_PerformMoreBuyAction_PerformMoreSellAction(self):
        config.maxGainFactor = 100
        evaluatedData = [
            EvaluatedData([1,2,3,4],True,2), 
            EvaluatedData([2,3,4,2],False,4), 
            EvaluatedData([2,3,4,2],True,1), 
            EvaluatedData([2,3,4,2],True,1), 
            EvaluatedData([2,3,4,2],True,1)]
        gain, buyAction, sellAction = performer.performStrategy(config, evaluatedData, sellStrategy = sellMockTrue)
        assert len(buyAction) == 3
        assert len(sellAction) == 2
    
    def test_PerformNoBuyAction_IfPriceIs0(self):
        config.maxGainFactor = 100
        evaluatedData = [
            EvaluatedData([1,2,3,4],True,0), 
            EvaluatedData([2,3,4,2],False,0), 
            EvaluatedData([2,3,4,2],True,0), 
            EvaluatedData([2,3,4,2],True,0), 
            EvaluatedData([2,3,4,2],True,0)]
        gain, buyAction, sellAction = performer.performStrategy(config, evaluatedData, sellStrategy = sellMockTrue)
        assert len(buyAction) == 0
        assert len(sellAction) == 0
    
    def test_PerformNoBuyAction_IfPriceIs0_ButElse(self):
        config.maxGainFactor = 100
        evaluatedData = [
            EvaluatedData([1,2,3,4],True,1), 
            EvaluatedData([2,3,4,2],False,2), 
            EvaluatedData([2,3,4,2],True,1), 
            EvaluatedData([2,3,4,2],True,2), 
            EvaluatedData([2,3,4,2],True,0)]
        gain, buyAction, sellAction = performer.performStrategy(config, evaluatedData, sellStrategy = sellMockTrue)
        assert len(buyAction) == 2
        assert len(sellAction) == 2