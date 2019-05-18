from Evaluation.PreEvaluation import preEvaluateData 
from Evaluation.PreEvaluation import evaluateBuyFallingSituation
from Evaluation.Performer import performStrategy as evaluateData
from Helpers.RandomWalkNumberGenerator import RandomWalker as walker
# import time 
import numpy as np

class StrategyMapper:

    maxRange = 1

    def __init__(self, maxRange):
        self.maxRange = maxRange


    def mapStategyToNumber(self, strat):
        return strat[0]* self.maxRange + strat[1]

    def mapNumberToStrategy(self, strat):
        limitFactor = strat % self.maxRange
        stopLoss = int((strat - limitFactor) / self.maxRange)
        return [stopLoss, limitFactor]

class StratResult:
    def __init__(self, gainArray, meanGain, strategy):
        self.gainArray = gainArray
        self.meanGain = meanGain
        self.strategy = strategy

def EvaluateStrategy(strategies, simulations, config, start, preEvaluation = preEvaluateData, evaluateData = evaluateData):
    mapper = StrategyMapper(config.maxRange)
    results = []
    # t0 = 0
    for strat in strategies:
        # t0 = time.thread_time()- t0
        # print('strat:', (t0), sep = '\t')
        gainArray = []
        config.stopLossFactor, config.sellAtFactor = mapper.mapNumberToStrategy(strat)
        # t1 = t0
        for sim in range(simulations):
            # t1 = time.thread_time()- t1
            # print('sim:', (t1), sep = '\t')
            rw = walker(start)
            data = rw.calcWalk(config.dataPoints)
            preparedData = preEvaluation(data, config.steps, evaluateBuyFallingSituation)
            gain =  evaluateData(config, preparedData, data)[0]
            gainArray.append(gain)
        results.append(StratResult(gainArray, np.mean(gainArray), strat))
    return results

def initStrategies(maxRange):
    strategies = []
    mapper = StrategyMapper(maxRange)
    for sellAtFactor in range(maxRange):
        for stopLossFactor in range(maxRange):
            if sellAtFactor > 0 and stopLossFactor > 0:
                strategies.append( mapper.mapStategyToNumber([sellAtFactor, stopLossFactor]))
    return strategies

def filterGoodStrategies(stratResults, filtervalue):
    filteredResultXStrategy = []
    filteredResultYMeanGain = []
    for res in stratResults:
        if res.meanGain > filtervalue:
            filteredResultYMeanGain.append(res.meanGain)
            filteredResultXStrategy.append(res.strategy)

    return [filteredResultXStrategy, filteredResultYMeanGain]

def filterBadStrategies(stratResults, filtervalue):
    filteredResultXStrategy = []
    filteredResultYMeanGain = []
    for res in stratResults:
        if not (res.meanGain > filtervalue):
            filteredResultYMeanGain.append(res.meanGain)
            filteredResultXStrategy.append(res.strategy)

    return [filteredResultXStrategy, filteredResultYMeanGain]
