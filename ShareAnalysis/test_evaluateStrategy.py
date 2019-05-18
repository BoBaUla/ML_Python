from Evaluation.EvaluateStrategy import *
from Helpers.RandomWalkNumberGenerator import RandomWalker as rw
from Helpers.Config import SimConfig
import pytest

# pytest test_evaluateStrategy.py

def test_StrategyMapper_mapNumberToStrategy():
    num = 11
    mapper = StrategyMapper(10)
    expectedResult = [1,1]
    
    result = mapper.mapNumberToStrategy(num)
    
    assert expectedResult == result

def test_StrategyMapper_mapStrategyToNumber():
    strat =  [1,1]
    mapper = StrategyMapper(10)
    expectedResult = 11
    
    result = mapper.mapStategyToNumber(strat)
    
    assert expectedResult == result

stratResult = StratResult([],10,[1,1])

def setupStratResults():
    stratResults = []
    stratResults.append(stratResult)
    return stratResults

def test_filterGoodStrategies_EmptyStrategies():
    stratResults = []
    minResult = 5
    config = SimConfig(invest = minResult)
    expectedResult = [[],[]]
    result = filterGoodStrategies(stratResults, config.invest)

    assert len(expectedResult) == len(result)

def test_filterGoodStrategies_NoGoodStrategies():
    stratResults = setupStratResults()
    minResult = 11
    config = SimConfig(invest = minResult)
    expectedResult = [[],[]]
    result = filterGoodStrategies(stratResults, config.invest)

    assert len(expectedResult) == len(result)

def test_filterGoodStrategies_NoneEmptyStrategies():
    stratResults = setupStratResults()
    minResult = 5
    config = SimConfig(invest = minResult)
    expectedResult = [[stratResult.strategy], [stratResult.meanGain]]
    result = filterGoodStrategies(stratResults, config.invest)

    assert len(expectedResult) == len(result)
    assert expectedResult == result

def test_filterBadStrategies_EmptyStrategies():
    stratResults = []
    minResult = 5
    config = SimConfig(invest = minResult)
    expectedResult = [[],[]]
    result = filterBadStrategies(stratResults, config.invest)

    assert len(expectedResult) == len(result)

def test_filterBadStrategies_NoBadStrategies():
    stratResults = setupStratResults()
    minResult = 1
    config = SimConfig(invest = minResult)
    expectedResult = [[],[]]
    result = filterBadStrategies(stratResults, config.invest)

    assert len(expectedResult) == len(result)

def test_filterBadStrategies_NoneEmptyStrategies():
    stratResults = setupStratResults()
    minResult = 50
    config = SimConfig(invest = minResult)
    expectedResult = [[stratResult.strategy], [stratResult.meanGain]]
    result = filterBadStrategies(stratResults, config.invest)

    assert expectedResult == result

simulations = 1
start = 10

def preEvaluateDataMock(data, steps, evaluationStrategy):
    return data

def evaluateDataMock(config, prepareData, data):
    return [0,1]

def test_EvaluateStrategy_ReturnsNothingAtEmptyStrategy():
    strategies = []
    
    result = EvaluateStrategy(strategies, simulations, SimConfig(maxRange=1), start, 
    preEvaluation = preEvaluateDataMock,
    evaluateData= evaluateDataMock)
    assert len(strategies) == len(result)

def test_EvaluateStrategy_ReturnsAtNoneEmptyStrategy():
    strategies = [11]

    result = EvaluateStrategy(strategies, simulations, SimConfig(maxRange=1), start, 
    preEvaluation = preEvaluateDataMock,
    evaluateData= evaluateDataMock)
    
    assert len(strategies) == len(result)


def test_EvaluateStrategy_ReturnsAtNoneEmptyStrategyMoreResults():
    strategies = [11,122,21]

    result = EvaluateStrategy(strategies, simulations, SimConfig(maxRange=1), start, 
    preEvaluation = preEvaluateDataMock,
    evaluateData= evaluateDataMock)

    assert len(strategies) == len(result)

def test_initStrategies():
    maxRange = 3
    expectedResult =[4,5,7,8]
    
    result = initStrategies(maxRange)

    assert expectedResult == result
    