import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import ShareAnalysisScipts.generator_randomwalk as rw 

from ShareAnalysisScipts.eva_Data_Types import EvaluationResult
from ShareAnalysisScipts.eva_PreEvaluation_Script import preEvaluateData
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
    
    if len(mem.meanMemory) == 0:
        return [0], [0], [0]

    for i in range(len(data)-steps):
        meanData.append(mem.meanMemory[i])
        upperStd.append(mem.meanMemory[i] + mem.stdMemory[i])
        lowerStd.append(mem.meanMemory[i] - mem.stdMemory[i])
    adjustToDataLengthWithRespectToSteps(steps, meanData)
    adjustToDataLengthWithRespectToSteps(steps, upperStd)
    adjustToDataLengthWithRespectToSteps(steps, lowerStd)
    return meanData, upperStd, lowerStd

def Run(configTrade,configWalker, evaluationStrategies, save = False):

    walker = rw.RandomWalker(configWalker)
    print('Config:', 
        'Invest\t' + str(configTrade.invest),
        'Fee\t' + str(configTrade.fee),
        'Mu\t' + str(configWalker.mu),
        'Sigma\t'+ str(configWalker.sigma),
        'SellAt\t'+ str(configTrade.sellAtFactor),
        'StoppL\t'+ str(configTrade.stopLossFactor),
        'Steps'+ str(configTrade.steps),
        sep = '\n')
    data = walker.calcWalk()
    fig, axs = plt.subplots(len(evaluationStrategies))

    for i in range(len(evaluationStrategies)):
        localEvaluatedData =  preEvaluateData(data, evaluationStrategies[i], configTrade.steps)
        localResults = performStrategy(configTrade, localEvaluatedData)

        meanData, upperSigma, lowerSigma = stdBordersForData(data, configTrade.steps)      

        plotResults(axs[i],evaluationStrategies[i].__name__ , data, localResults)
        if len(meanData) > 1:
            plotData(axs[i], data, description = 'mu', subdata = [range(len(data)-1),meanData], subdataColor='r--')
            plotData(axs[i], data, description = 'mu + sigma', subdata = [range(len(data)-1),upperSigma], subdataColor='y-')
            plotData(axs[i], data, description = 'mu - sigma', subdata = [range(len(data)-1),lowerSigma], subdataColor='y-')
            mem.resetAll()

        if save:
            evaRes = EvaluationResult(data, localResults, configTrade, evaluationStrategies[i].__name__)
            evaRes.Save()
        
    plt.show()

