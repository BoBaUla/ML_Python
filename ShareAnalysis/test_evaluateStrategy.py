from Evaluation.EvaluateStrategy import *
from Helpers.RandomWalkNumberGenerator import RandomWalker as rw
from Helpers.Config import SimConfig
import pytest


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

def test_filterGoodStrategies_EmptyStrategies():
    stratResults = []
    minResult = 5
    config = SimConfig(invest = minResult)
    expectedResult = [[],[]]
    result = filterGoodStrategies(stratResults, config, config.invest)

    assert expectedResult == result

def test_filterGoodStrategies_NoGoodStrategies():
    stratResults = [[10,[1,1]],[10,[2,1]],[1,[1,2]]]
    minResult = 11
    config = SimConfig(invest = minResult)
    expectedResult = [[],[]]
    result = filterGoodStrategies(stratResults, config, config.invest)

    assert expectedResult == result

def test_filterGoodStrategies_NoneEmptyStrategies():
    stratResults = [[10,[1,1]],[10,[2,1]],[1,[1,2]]]
    minResult = 5
    config = SimConfig(invest = minResult)
    expectedResult = [[11,21],[10,10]]
    result = filterGoodStrategies(stratResults, config, config.invest)

    assert expectedResult == result

def test_filterBadStrategies_EmptyStrategies():
    stratResults = []
    minResult = 5
    config = SimConfig(invest = minResult)
    expectedResult = [[],[]]
    result = filterBadStrategies(stratResults, config, config.invest)

    assert expectedResult == result

def test_filterBadStrategies_NoBadStrategies():
    stratResults = [[10,[1,1]],[10,[2,1]],[2,[1,2]]]
    minResult = 1
    config = SimConfig(invest = minResult)
    expectedResult = [[],[]]
    result = filterBadStrategies(stratResults, config, config.invest)

    assert expectedResult == result

def test_filterBadStrategies_NoneEmptyStrategies():
    stratResults = [[10,[1,1]],[10,[2,1]],[1,[1,2]]]
    minResult = 5
    config = SimConfig(invest = minResult)
    expectedResult = [[12],[1]]
    result = filterBadStrategies(stratResults, config, config.invest)

    assert expectedResult == result

def test_EvaluateStrategy_ReturnsNothingAtEmptyStrategy():
    strategies = []
    walker = rw(10)
    simulations = 1

    result = EvaluateStrategy(strategies, walker, simulations, SimConfig())

    assert len(strategies) == len(result)

def test_EvaluateStrategy_ReturnsAtNoneEmptyStrategy():
    strategies = [11]
    walker = rw(10)
    simulations = 1

    result = EvaluateStrategy(strategies, walker, simulations, SimConfig())

    assert len(strategies) == len(result)

def test_EvaluateStrategy_ReturnsAtNoneEmptyStrategyMoreResults():
    strategies = [11,122,21]
    walker = rw(10)
    simulations = 1

    result = EvaluateStrategy(strategies, walker, simulations, SimConfig())

    assert len(strategies) == len(result)
