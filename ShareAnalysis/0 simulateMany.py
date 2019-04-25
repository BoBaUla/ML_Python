import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import Helpers.PlottingCollection as pc 
import Helpers.mathHelper as mh 
import Helpers.WeightsHelper as wh 
import Helpers.RandomWalkNumberGenerator as rw 

from Helpers.Config import SimConfig
from Evaluation.PreEvaluation import EndIntervallEvaluation as preEvaluateData
from Evaluation.Performer import performStrategy
import Helpers.RandomWalkNumberGenerator as rw 

gainArray = []
config = SimConfig(sellAtFactor=0.05, stopLossFactor=0.05 )
config.mu = np.random.randint(-100,100)/100
simulations = 100


for i in range(simulations):
    walker = rw.RandomWalker(config.init, config.mu, config.sigma, 0.2)
    data = walker.calcWalk(config.dataPoints)
    preparedData = preEvaluateData(data, config.steps)
    gainArray.append(performStrategy(config, preparedData , data)[0])


avg = np.mean(gainArray)
std = np.std(gainArray)
mid = np.median(gainArray)
p0 = mh.getRelationLargerThan(avg, gainArray)
p1 = mh.getRelationLargerThan(mid, gainArray)

print('WSK: ' + str(p0 * 100),'Ctl: ' + str(p1*100) ,'AVG: ' + str(avg),'MID: ' +str(mid),'STD: ' + str(std), sep = '\n')
plt.plot(gainArray)
plt.grid()
plt.show()