import EvaluateStrategy as es
from Config import SimConfig
import matplotlib.pyplot as plt # plotten von daten
import PlottingCollection as pcol
import numpy as np 

@staticmethod
def Run(dataPoints, dataEvaluationLength, strategyRange, randomWalkerStart, randomWalkerMu, randomWalkerSigma, capital):
    config = SimConfig(
        maxStrategyRange = strategyRange, 
        dataPoints = dataPoints, 
        init = randomWalkerStart,
        mu = randomWalkerMu,
        sigma = randomWalkerSigma,
        invest = capital,
        fee = 5,
        steps=dataEvaluationLength)

    simulations = 5

    strategies = es.initLimitStrategies(config.maxStrategyRange)
    evaluations = len(strategies) * simulations
    print( str(evaluations)+ '\t evaluations')

    evalutatedStrategies = es.EvaluateStrategy(strategies, simulations, config, config.init)
    goodStrategies = es.filterGoodStrategies(evalutatedStrategies, config.invest)
    badStrategies = es.filterBadStrategies(evalutatedStrategies, config.invest)

    fig, axs = plt.subplots(2,2)

    pcol.plotHist(goodStrategies[0], axs[0][1], 1,  color = 'green', title = 'Limits')
    pcol.plotHist(goodStrategies[1], axs[1][1], 5,  color = 'green', title = 'Resultate')

    pcol.plotHist(badStrategies[0], axs[0][0], 1, color= 'red', title = 'Limits')
    pcol.plotHist(badStrategies[1], axs[1][0], 5, color= 'red', title = 'Resultate')

    plt.show()