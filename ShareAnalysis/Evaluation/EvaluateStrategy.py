from Evaluation.PreEvaluation import preEvaluateData 
from Evaluation.PreEvaluationStrategies import evaluateByFallingSituation
from Evaluation.Performer import performStrategy as performer
from Helpers.RandomWalkNumberGenerator import RandomWalker as walker
import time 
import numpy as np

class StrategyMapper:

    maxRange = 1

    def __init__(self, maxStrategyRange):
        self.maxStrategyRange = maxStrategyRange


    def mapStategyToNumber(self, strat):
        return strat[0]* self.maxStrategyRange + strat[1]

    def mapNumberToStrategy(self, strat):
        sellAt = strat % self.maxStrategyRange
        stopLoss = int((strat - sellAt) / self.maxStrategyRange)
        return [stopLoss, sellAt]

class StratResult:
    def __init__(self, gainArray, meanGain, strategy):
        self.gainArray = gainArray
        self.meanGain = meanGain
        self.strategy = strategy

def EvaluateStrategy(strategies, simulations, config, start, preEvaluation = preEvaluateData, performer = performer):
    mapper = StrategyMapper(config.maxStrategyRange)
    results = []
    t0 =  time.time()
    durationFactor = np.sqrt(len(strategies))
    printed = False
    count = 0
    for strat in strategies:
        count = count + 1
        gainArray = []
        stopLoss, sellAt = mapper.mapNumberToStrategy(strat)
        config.stopLossFactor = stopLoss / 100
        config.sellAtFactor = sellAt / 100
        # t1 = t0
        for sim in range(simulations):
            # t1 = time.thread_time()- t1
            # print('sim:', (t1), sep = '\t')
            rw = walker(start)
            data = rw.calcWalk(config.dataPoints)
            preparedData = preEvaluation(data, evaluateByFallingSituation, config.steps)
            gain =  performer(config, preparedData)[0]
            gainArray.append(gain)
        results.append(StratResult(gainArray, np.mean(gainArray), strat))
        t =  time.time() - t0
        if not printed:
            print('estimated duration:', (durationFactor -1)* t * 10, 's', sep = '\t')
            printed = True
        print('strat:', count, 'from', len(strategies), 'duration', np.round(t,2), 's', 'mean result:', results[count-1].meanGain, sep = '\t')

    return results

def initLimitStrategies(maxStrategyRange):
    strategies = []
    mapper = StrategyMapper(maxStrategyRange)
    for sellAtFactor in range(maxStrategyRange):
        for stopLossFactor in range(maxStrategyRange):
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
