from Evaluation.EvaluateStrategy import *
from Helpers.Config import SimConfig
import matplotlib.pyplot as plt # plotten von daten
from Helpers import PlottingCollection as pcol
import numpy as np 

config = SimConfig(
    maxStrategyRange=10, 
    dataPoints=500, 
    init=np.random.randint(50,150),
    mu= 0,
    sigma= 0.4,
    invest=1000,
    fee = 5,
    steps=50)

simulations = 5

strategies = initStrategies(config.maxStrategyRange)
evaluations = len(strategies) * simulations
print( str(evaluations)+ '\t evaluations')

evalutatedStrategies = EvaluateStrategy(strategies, simulations, config, config.init)
goodStrategies = filterGoodStrategies(evalutatedStrategies, config.invest)
badStrategies = filterBadStrategies(evalutatedStrategies, config.invest)

fig, axs = plt.subplots(2,2)

pcol.plotHist(goodStrategies[0], axs[0][1], 1,  color = 'green')
pcol.plotHist(goodStrategies[1], axs[1][1], 5,  color = 'green')

pcol.plotHist(badStrategies[0], axs[0][0], 1, color= 'red')
pcol.plotHist(badStrategies[1], axs[1][0], 5, color= 'red')

plt.show()