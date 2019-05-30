import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import Helpers.PlottingCollection as pc 
import Helpers.mathHelper as mh 
import Helpers.WeightsHelper as wh 
import Helpers.RandomWalkNumberGenerator as rw 
from Helpers.Config import SimConfig

from Evaluation.EvaluateStrategy import *
from Evaluation.Performer import performStrategy

from Evaluation.PreEvaluation import preEvaluateData
from Evaluation.PreEvaluationStrategies import endIntervallEvaluation as evaluation

gainArray = []
result = []
config = SimConfig(
    mu= np.random.randint(-100,100)/100,
    sellAtFactor=0.05, 
    stopLossFactor=0.05,
    maxStrategyRange=13)
    
strategies = initStrategies(config.maxStrategyRange)
mapper = StrategyMapper(config.maxStrategyRange)

walker = rw.RandomWalker(config.init, config.mu, config.sigma, 0.2)
data = walker.calcWalk(config.dataPoints)

for i in strategies:  
    stopLossFactor, sellAtFactor = mapper.mapNumberToStrategy(i)
    config.stopLossFactor = stopLossFactor/100
    config.sellAtFactor = sellAtFactor/100
    preparedData = preEvaluateData(data, evaluation, config.steps)
    gain = performStrategy(config, preparedData)[0]
    print(i, config.stopLossFactor, config.sellAtFactor, gain, sep = '\t')
    gainArray.append(gain)
    result.append(StratResult(gain, gain, i))

goodStrategies = filterGoodStrategies(result, config.invest)
badStrategies = filterBadStrategies(result, config.invest)

avg = np.mean(gainArray)
std = np.std(gainArray)
mid = np.median(gainArray)
p0 = mh.getRelationLargerThan(avg, gainArray)
p1 = mh.getRelationLargerThan(mid, gainArray)

fig, axs = plt.subplots(2,3)

print('WSK: ' + str(p0 * 100),'Ctl: ' + str(p1*100) ,'AVG: ' + str(avg),'MID: ' +str(mid),'STD: ' + str(std), sep = '\n')
axs[0][0].plot(data, label = 'Data')
axs[0][0].grid()

axs[1][0].plot(gainArray, label = 'Results')
axs[1][0].grid()

pc.plotHist(goodStrategies[0], axs[1][1], 1,  color = 'green')
pc.plotHist(goodStrategies[1], axs[1][2], 5,  color = 'green')

pc.plotHist(badStrategies[0], axs[0][1], 1, color= 'red')
pc.plotHist(badStrategies[1], axs[0][2], 5, color= 'red')
plt.show()

