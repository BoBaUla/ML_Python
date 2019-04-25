from Evaluation.PreEvaluation import EndIntervallEvaluation as preEvaluateData
from Evaluation.Performer import performStrategy as evaluateData
from Helpers.RandomWalkNumberGenerator import RandomWalker as walker

class StrategyMapper:

    def __init__(self, maxRange):
        self.maxRange = maxRange


    def mapStategyToNumber(self, strat):
        return strat[0]* self.maxRange + strat[1]

    def mapNumberToStrategy(self, strat):
        limitFactor = strat % self.maxRange
        stopLoss = int((strat - limitFactor) / self.maxRange)
        return [stopLoss, limitFactor]

def EvaluateStrategy(strategies, simulations, config, start):
    mapper = StrategyMapper(config.maxRange)
    results = []
    for strat in strategies:
        gainArray = []
        config.stopLossFactor, config.sellAtFactor = mapper.mapNumberToStrategy(strat)
        for sim in range(simulations):
            rw = walker(start)
            data = rw.calcWalk(config.dataPoints)
            preparedData = preEvaluateData(data, config.steps)
            gainArray.append(evaluateData(config, preparedData, data)[0])
        results.append([gainArray, strat])  
    return results

def initStrategies(maxRange):
    strategies = []
    for sellAtFactor in range(maxRange):
        for stopLossFactor in range(maxRange):
            if sellAtFactor > 0 and stopLossFactor > 0:
                strategies.append([sellAtFactor, stopLossFactor])
    return strategies

def filterGoodStrategies(stratResults, config, filtervalue):
    mapper = StrategyMapper(config.maxRange)
    filteredResultX = []
    filteredResultY = []
    for res in stratResults:
        if res[0] > filtervalue:
            filteredResultY.append(res[0])
            filteredResultX.append(mapper.mapStategyToNumber(res[1]))
            
    return [filteredResultX, filteredResultY]

def filterBadStrategies(results, config, filtervalue):
    mapper = StrategyMapper(config.maxRange)
    filteredResultX = []
    filteredResultY = []
    for res in results:
            if not (res[0] > filtervalue):
                    filteredResultY.append(res[0])
                    filteredResultX.append(mapper.mapStategyToNumber(res[1]))
    return [filteredResultX, filteredResultY]