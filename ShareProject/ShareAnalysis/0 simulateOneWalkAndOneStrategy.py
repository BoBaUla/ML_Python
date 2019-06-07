import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import Helpers.RandomWalkNumberGenerator as rw 

from Helpers.Config import SimConfig
from Evaluation.PreEvaluation import preEvaluateData
from Evaluation.PreEvaluationStrategies import *
from Evaluation.Performer import performStrategy
from Helpers.PlottingCollection import plotResults



config = SimConfig(
    sellAtFactor=0.04, 
    stopLossFactor=0.06, 
    steps= 10,
    mu = np.random.randint(-100,100)/100,
    sigma =5)

walker = rw.RandomWalker(config.init, config.mu, config.sigma, 0.2)
data = walker.calcWalk(config.dataPoints)

startPreparedData = preEvaluateData(data, startIntervallEvaluation, config.steps)
startResults = performStrategy(config, startPreparedData)

endPreparedData =   preEvaluateData(data, endIntervallEvaluation, config.steps)
endResults = performStrategy(config, endPreparedData)

fallingPreparedData =   preEvaluateData(data, evaluateByFallingSituation, config.steps)
fallingResults = performStrategy(config, fallingPreparedData)

risingPreparedData =   preEvaluateData(data, evaluateByRisingSituation, config.steps)
risingResults = performStrategy(config, risingPreparedData)

linearRisingPrepareData =  preEvaluateData(data, linearInterpolationRisingEvaluation, config.steps)
linearRisingResults = performStrategy(config, linearRisingPrepareData)

linearFallingPrepareData =  preEvaluateData(data, linearInterpolationFallingEvaluation, config.steps)
linearFallingResults = performStrategy(config, linearFallingPrepareData)

squareMinPrepareData =  preEvaluateData(data, squareInterpolation_HasMinimumEvaluation, config.steps)
squareMinResults = performStrategy(config, squareMinPrepareData)

squareMaxPrepareData =  preEvaluateData(data, squareInterpolation_HasMaximumEvaluation, config.steps)
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

