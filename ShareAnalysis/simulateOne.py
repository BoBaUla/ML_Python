import matplotlib.pyplot as plt # plotten von daten
import numpy as np 

from Helpers.Config import SimConfig
from Evaluation.PreEvaluation import preEvaluateData
from Evaluation.Performer import performStrategy
import Helpers.RandomWalkNumberGenerator as rw 

config = SimConfig()

walker = rw.RandomWalker(config.init, config.mu, config.sigma, 0.2)
data = walker.calcWalk(config.dataPoints)
preparedData = preEvaluateData(data, config.steps)
[gain, buy, sell] = performStrategy(config.invest, config.fee, preparedData , data, config.steps, limitFactor= config.sellAtFactor, stopLossFactor=config.stopLossFactor)

if len(buy) > 0:
    buyX = np.array(buy)[:,0]
    buyY = np.array(buy)[:,1]
if len(sell) > 0:
    sellX = np.array(sell)[:,0]
    sellY = np.array(sell)[:,1]

fig, axs = plt.subplots(2,1)

axs[0].plot(data, 'k-')
axs[0].plot(buyX, buyY, 'go', label = 'buy')
axs[0].plot(sellX, sellY, 'rx', label = 'sell')
axs[0].legend()

print(gain)
plt.show()

# imax = max(len(sell,len(buy))
# for i in range(imax):
#     print(buy[i], sell[i])