import matplotlib.pyplot as plt # plotten von daten
import numpy as np 

from Helpers.Config import SimConfig
from Evaluation.PreEvaluation import preEvaluateData
from Evaluation.Performer import performStrategy
import Helpers.RandomWalkNumberGenerator as rw 

config = SimConfig(sellAtFactor=0.06, stopLossFactor=0.01 )
config.mu = np.random.randint(-100,100)/100
walker = rw.RandomWalker(config.init, config.mu, config.sigma, 0.2)
data = walker.calcWalk(config.dataPoints)
preparedData = preEvaluateData(data, config.steps)
[gain, buy, sell] = performStrategy(config.invest, config.fee, preparedData , data, config.steps, limitFactor= config.sellAtFactor, stopLossFactor=config.stopLossFactor)

fig, axs = plt.subplots(2,1)

axs[0].plot(data, 'k-')

if len(buy) > 0:
    buyX = np.array(buy)[:,0]
    buyY = np.array(buy)[:,1]
    axs[0].plot(buyX, buyY, 'go', label = 'buy')

if len(sell) > 0:
    sellX = np.array(sell)[:,0]
    sellY = np.array(sell)[:,1]
    axs[0].plot(sellX, sellY, 'rx', label = 'sell')

axs[0].legend()

axs[0].grid()

print(gain)
plt.show()
