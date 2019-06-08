from ShareAnalysisScipts.helper_Weights import ExpectedValue
from ShareAnalysisScipts.helper_Math import linearInterpolation, squareInterpolation
import numpy as np 

def getLastValue(subset):
    return subset[len(subset) - 1]

def evaluateByFallingSituation(subset):
    return ExpectedValue(subset,1) > getLastValue(subset)

def evaluateByRisingSituation(subset):
    return ExpectedValue(subset,1) < getLastValue(subset)

def endIntervallEvaluation(subset):
    return subset[0] < getLastValue(subset)

def startIntervallEvaluation(subset):
    return subset[0] > getLastValue(subset)

def linearInterpolationRisingEvaluation(subset):
    return linearInterpolation(subset)[0] > 0

def linearInterpolationFallingEvaluation(subset):
    return linearInterpolation(subset)[0] < 0

def squareInterpolation_HasMinimumEvaluation(subset):
    return squareInterpolation(subset)[0] > 0

def squareInterpolation_HasMaximumEvaluation(subset):
    return squareInterpolation(subset)[0] < 0

memory = [0]
def buyAtLocalMinimum_Evaluation(subset, steps = 1):
    minValue = min(subset)
    lastValue = getLastValue(subset)
    memory.append(lastValue)
    if len(memory) < steps:
        for step in range(steps-1):
            memory.append(subset[step])
    
    meanMemory = np.mean(memory)
    stdMemory = np.std(memory)
    return lastValue == minValue and (lastValue < meanMemory - stdMemory)

