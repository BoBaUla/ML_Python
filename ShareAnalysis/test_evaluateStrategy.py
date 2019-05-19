from Evaluation.EvaluateStrategy import *
from Helpers.RandomWalkNumberGenerator import RandomWalker as rw
from Helpers.Config import SimConfig
import pytest

# pytest test_evaluateStrategy.py
class TestMapper(object):
    def test_StrategyMapper_mapNumberToStrategy(self):
        num = 11
        mapper = StrategyMapper(10)
        expectedResult = [1,1]
        
        result = mapper.mapNumberToStrategy(num)
        
        assert expectedResult == result

    def test_StrategyMapper_mapStrategyToNumber(self):
        strat =  [1,1]
        mapper = StrategyMapper(10)
        expectedResult = 11
        
        result = mapper.mapStategyToNumber(strat)
        
        assert expectedResult == result

class TestFilterStrategies(object):
    stratResult = StratResult([],10,[1,1])

    def setupStratResults(self):
        stratResults = []
        stratResults.append(self.stratResult)
        return stratResults

    def test_filterGoodStrategies_EmptyStrategies(self):
        stratResults = []
        minResult = 5
        config = SimConfig(invest = minResult)
        expectedResult = [[],[]]
        result = filterGoodStrategies(stratResults, config.invest)

        assert len(expectedResult) == len(result)

    def test_filterGoodStrategies_NoGoodStrategies(self):
        stratResults = self.setupStratResults()
        minResult = 11
        config = SimConfig(invest = minResult)
        expectedResult = [[],[]]
        result = filterGoodStrategies(stratResults, config.invest)

        assert len(expectedResult) == len(result)

    def test_filterGoodStrategies_NoneEmptyStrategies(self):
        stratResults = self.setupStratResults()
        minResult = 5
        config = SimConfig(invest = minResult)
        expectedResult = [[self.stratResult.strategy], [self.stratResult.meanGain]]
        result = filterGoodStrategies(stratResults, config.invest)

        assert len(expectedResult) == len(result)
        assert expectedResult == result

    def test_filterBadStrategies_EmptyStrategies(self):
        stratResults = []
        minResult = 5
        config = SimConfig(invest = minResult)
        expectedResult = [[],[]]
        result = filterBadStrategies(stratResults, config.invest)

        assert len(expectedResult) == len(result)

    def test_filterBadStrategies_NoBadStrategies(self):
        stratResults = self.setupStratResults()
        minResult = 1
        config = SimConfig(invest = minResult)
        expectedResult = [[],[]]
        result = filterBadStrategies(stratResults, config.invest)

        assert len(expectedResult) == len(result)

    def test_filterBadStrategies_NoneEmptyStrategies(self):
        stratResults = self.setupStratResults()
        minResult = 50
        config = SimConfig(invest = minResult)
        expectedResult = [[self.stratResult.strategy], [self.stratResult.meanGain]]
        result = filterBadStrategies(stratResults, config.invest)

        assert expectedResult == result

class TestEvaluateStrategy(object):
    simulations = 1
    start = 10

    def preEvaluateDataMock(self,data, steps, evaluationStrategy):
        return data

    def evaluateDataMock(self,config, prepareData):
        return [0,1]

    def test_EvaluateStrategy_ReturnsNothingAtEmptyStrategy(self):
        strategies = []
        
        result = EvaluateStrategy(strategies, self.simulations, SimConfig(maxStrategyRange=1), self.start, 
        preEvaluation = self.preEvaluateDataMock,
        performer = self.evaluateDataMock)
        assert len(strategies) == len(result)

    def test_EvaluateStrategy_ReturnsAtNoneEmptyStrategy(self):
        strategies = [11]

        result = EvaluateStrategy(strategies, self.simulations, SimConfig(maxStrategyRange=1), self.start, 
        preEvaluation = self.preEvaluateDataMock,
        performer = self.evaluateDataMock)
        
        assert len(strategies) == len(result)


    def test_EvaluateStrategy_ReturnsAtNoneEmptyStrategyMoreResults(self):
        strategies = [11,122,21]

        result = EvaluateStrategy(strategies, self.simulations, SimConfig(maxStrategyRange=1), self.start, 
        preEvaluation = self.preEvaluateDataMock,
        performer = self.evaluateDataMock)

        assert len(strategies) == len(result)

class TestInitStrategies(object):
    
    def test_initStrategies(self):
        maxRange = 3
        expectedResult =[4,5,7,8]
        
        result = initStrategies(maxRange)

        assert expectedResult == result
    