import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import ShareAnalysisScipts.generator_randomwalk as rw 

from ShareAnalysisScipts.eva_PreEvaluation_Script import preEvaluateData
import ShareAnalysisScipts.eva_PreEvaluationStrategies  as pes
from ShareAnalysisScipts.eva_Performer import performStrategy
from ShareAnalysisScipts.plot_ScriptCollection import plotResults



def Run(configTrade,configWalker):
    walker = rw.RandomWalker(configWalker)
    data = walker.calcWalk()

    startPreparedData = preEvaluateData(data, pes.startIntervallEvaluation, configTrade.steps)
    startResults = performStrategy(configTrade, startPreparedData)

    endPreparedData =   preEvaluateData(data, pes.endIntervallEvaluation, configTrade.steps)
    endResults = performStrategy(configTrade, endPreparedData)

    fallingPreparedData =   preEvaluateData(data, pes.evaluateByFallingSituation, configTrade.steps)
    fallingResults = performStrategy(configTrade, fallingPreparedData)

    risingPreparedData =   preEvaluateData(data, pes.evaluateByRisingSituation, configTrade.steps)
    risingResults = performStrategy(configTrade, risingPreparedData)

    linearRisingPrepareData =  preEvaluateData(data, pes.linearInterpolationRisingEvaluation, configTrade.steps)
    linearRisingResults = performStrategy(configTrade, linearRisingPrepareData)

    linearFallingPrepareData =  preEvaluateData(data, pes.linearInterpolationFallingEvaluation, configTrade.steps)
    linearFallingResults = performStrategy(configTrade, linearFallingPrepareData)

    squareMinPrepareData =  preEvaluateData(data, pes.squareInterpolation_HasMinimumEvaluation, configTrade.steps)
    squareMinResults = performStrategy(configTrade, squareMinPrepareData)

    squareMaxPrepareData =  preEvaluateData(data, pes.squareInterpolation_HasMaximumEvaluation, configTrade.steps)
    squareMaxResults = performStrategy(configTrade, squareMaxPrepareData)

    fig, axs = plt.subplots(2,4)

    plotResults(axs[0][0],'startIntervallEvaluation', data, startResults)
    plotResults(axs[1][0],'endIntervallEvaluation', data, endResults)
    plotResults(axs[0][1],'evaluateByFallingSituation', data, fallingResults)
    plotResults(axs[1][1],'evaluateByRisingSituation', data, risingResults)
    plotResults(axs[0][2],'linearInterpolationRisingEvaluations', data, linearRisingResults)
    plotResults(axs[1][2],'linearInterpolationFallingEvaluation', data, linearFallingResults)
    plotResults(axs[0][3],'squareInterpolation_HasMinimumEvaluation', data, squareMinResults)
    plotResults(axs[1][3],'squareInterpolation_HasMaximumEvaluation', data, squareMaxResults)
    plt.show()

