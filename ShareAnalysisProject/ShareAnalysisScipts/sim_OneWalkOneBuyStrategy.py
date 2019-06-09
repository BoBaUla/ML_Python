import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import ShareAnalysisScipts.generator_randomwalk as rw 

from ShareAnalysisScipts.config_Type import SimConfig
from ShareAnalysisScipts.eva_PreEvaluation_Script import preEvaluateData
from ShareAnalysisScipts.eva_PreEvaluationStrategies import *
from ShareAnalysisScipts.eva_Performer import performStrategy
from ShareAnalysisScipts.plot_ScriptCollection import plotResults, plotData
import ShareAnalysisScipts.eva_Memory as mem

def adjustToDataLengthWithRespectToSteps(steps, dataToAdjust):
    for i in range(steps-1):
        dataToAdjust.insert(0, dataToAdjust[0])

def stdBordersForData(data, steps):
    meanData = []
    upperStd = []
    lowerStd = []
    
    for i in range(len(data)-steps):
        meanData.append(mem.meanMemory[i])
        upperStd.append(mem.meanMemory[i] + mem.stdMemory[i])
        lowerStd.append(mem.meanMemory[i] - mem.stdMemory[i])
    adjustToDataLengthWithRespectToSteps(steps, meanData)
    adjustToDataLengthWithRespectToSteps(steps, upperStd)
    adjustToDataLengthWithRespectToSteps(steps, lowerStd)
    return meanData, upperStd, lowerStd

def Run(config, evaluationStrategies):

    walker = rw.RandomWalker(config.init, config.mu, config.sigma)
    data = walker.calcWalk(config.dataPoints)
    fig, axs = plt.subplots(len(evaluationStrategies))

    for i in range(len(evaluationStrategies)):
        localEvaluatedData =  preEvaluateData(data, evaluationStrategies[i], config.steps)
        localResults = performStrategy(config, localEvaluatedData)

        meanData, upperSigma, lowerSigma = stdBordersForData(data, config.steps)      

        plotResults(axs[i],evaluationStrategies[i].__name__ , data, localResults)
        plotData(axs[i], data, description = 'mu', subdata = [range(len(data)-1),meanData], subdataColor='r--')
        plotData(axs[i], data, description = 'mu + sigma', subdata = [range(len(data)-1),upperSigma], subdataColor='y.')
        plotData(axs[i], data, description = 'mu - sigma', subdata = [range(len(data)-1),lowerSigma], subdataColor='y.')
        mem.resetAll()
    plt.show()

