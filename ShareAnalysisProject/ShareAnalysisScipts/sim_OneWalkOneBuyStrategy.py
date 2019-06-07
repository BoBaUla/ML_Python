import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import generator_randomwalk as rw 

from config_Type import SimConfig
from eva_PreEvaluation_Script import preEvaluateData
from eva_PreEvaluationStrategies import *
from eva_Performer import performStrategy
from plot_ScriptCollection import plotResults, plotData

def stdBordersForData(data):
    meanData = []
    upperStd = []
    underStd = []
    for i in range(len(data)-1):
        subdata = data[0:i]
        mean = np.mean(subdata)
        meanData.append(mean)
        upperStd.append(mean + np.std(subdata))
        underStd.append(mean - np.std(subdata))
    return meanData, upperStd, underStd

config = SimConfig(
    sellAtFactor=0.04, 
    stopLossFactor=0.06, 
    steps= 50,
    mu = np.random.randint(-100,100)/100,
    sigma =5)

walker = rw.RandomWalker(config.init, config.mu, config.sigma, 0.2)
data = walker.calcWalk(config.dataPoints)

localMinEvaluatedData =  preEvaluateData(data, buyAtLocalMinimum_Evaluation, config.steps)
localMinResults = performStrategy(config, localMinEvaluatedData)

meanData, upperSigma, lowerSigma = stdBordersForData(data)

fig, axs = plt.subplots(2)

plotResults(axs[0],'localMinEvaluatedData', data, localMinResults)
plotData(axs[0],'localMinEvaluatedData', data, [range(len(data)-1),meanData], subdataColor='r--')
plotData(axs[0],'localMinEvaluatedData', data, [range(len(data)-1),upperSigma], subdataColor='g.')
plotData(axs[0],'localMinEvaluatedData', data, [range(len(data)-1),lowerSigma], subdataColor='g.')
plt.show()

