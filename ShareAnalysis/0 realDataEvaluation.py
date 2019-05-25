import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import Helpers.PlottingCollection as pc 
import Helpers.mathHelper as mh
from Helpers.ReadingData import readData
from Helpers.Config import SimConfig
from Evaluation.PreEvaluation import  startIntervallEvaluation, preEvaluateData
from Evaluation.Performer import performStrategy
# 
# GEHT LEIDER NOCH NICHT!
#  


workingfiles = [
'A0LEW8_MRZ_01.csv',
]

config = SimConfig(
        steps = 50,
        stopLossFactor =0.01,
        sellAtFactor= 0.09,
        fee = 5
        )

for i in workingfiles:
    data =  readData(i)
    prepateredData = preEvaluateData(data, config.steps, startIntervallEvaluation)
    [gain, buy, sell] = performStrategy(config , prepateredData)
    if len(buy) >0 and len(sell)>0:
        buyX = np.array(buy)[:,0]
        buyY = np.array(buy)[:,1]

        sellX = np.array(sell)[:,0]
        sellY = np.array(sell)[:,1]


        fig, axs = plt.subplots(2,1)
        fig.title = i
        axs[0].plot(data, 'k-')
        axs[0].plot(buyX, buyY, 'go', label = 'buy')
        axs[0].plot(sellX, sellY, 'rx', label = 'sell')

        d = mh.returnFromData(data)
        axs[1].plot(d, 'k-')
        axs[0].legend()      
        print(gain)
        plt.show()
