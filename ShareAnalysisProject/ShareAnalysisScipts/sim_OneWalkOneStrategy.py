import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import generator_randomwalk as rw 

from config_Type import SimConfig
from eva_PreEvaluation_Script import preEvaluateData
import eva_PreEvaluationStrategies  as pes
from eva_Performer import performStrategy
from plot_ScriptCollection import plotResults



config = SimConfig(
    sellAtFactor=0.04, 
    stopLossFactor=0.06, 
    steps= 10,
    mu = np.random.randint(-100,100)/100,
    sigma =5)

walker = rw.RandomWalker(config.init, config.mu, config.sigma, 0.2)
data = walker.calcWalk(config.dataPoints)

startPreparedData = preEvaluateData(data, pes.startIntervallEvaluation, config.steps)
startResults = performStrategy(config, startPreparedData)

endPreparedData =   preEvaluateData(data, pes.endIntervallEvaluation, config.steps)
endResults = performStrategy(config, endPreparedData)

fallingPreparedData =   preEvaluateData(data, pes.evaluateByFallingSituation, config.steps)
fallingResults = performStrategy(config, fallingPreparedData)

risingPreparedData =   preEvaluateData(data, pes.evaluateByRisingSituation, config.steps)
risingResults = performStrategy(config, risingPreparedData)

linearRisingPrepareData =  preEvaluateData(data, pes.linearInterpolationRisingEvaluation, config.steps)
linearRisingResults = performStrategy(config, linearRisingPrepareData)

linearFallingPrepareData =  preEvaluateData(data, pes.linearInterpolationFallingEvaluation, config.steps)
linearFallingResults = performStrategy(config, linearFallingPrepareData)

squareMinPrepareData =  preEvaluateData(data, pes.squareInterpolation_HasMinimumEvaluation, config.steps)
squareMinResults = performStrategy(config, squareMinPrepareData)

squareMaxPrepareData =  preEvaluateData(data, pes.squareInterpolation_HasMaximumEvaluation, config.steps)
squareMaxResults = performStrategy(config, squareMaxPrepareData)

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

