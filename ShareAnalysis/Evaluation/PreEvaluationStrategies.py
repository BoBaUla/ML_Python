from Helpers.WeightsHelper import ExpectedValue
from Helpers.mathHelper import linearInterpolation, squareInterpolation
import numpy as np 

def getLastValue(subset, steps):
    return subset[steps - 1]

def evaluateByFallingSituation(subset, steps):
    return ExpectedValue(subset,1) > getLastValue(subset, steps)

def evaluateByRisingSituation(subset, steps):
    return ExpectedValue(subset,1) < getLastValue(subset, steps)

def endIntervallEvaluation(subset, steps = 1):
    return subset[0] < getLastValue(subset, steps)

def startIntervallEvaluation(subset, steps = 1):
    return subset[0] > getLastValue(subset, steps)

def linearInterpolationRisingEvaluation(subset, steps = 1):
    return linearInterpolation(subset)[0] > 0

def linearInterpolationFallingEvaluation(subset, steps = 1):
    return linearInterpolation(subset)[0] < 0

def squareInterpolation_HasMinimumEvaluation(subset, steps = 1):
    return squareInterpolation(subset)[0] > 0

def squareInterpolation_HasMaximumEvaluation(subset, steps = 1):
    return squareInterpolation(subset)[0] < 0

memory = [0]
def buyAtLocalMinimum_Evaluation(subset, steps = 1):
    minValue = min(subset)
    lastValue = getLastValue(subset, steps)
    memory.append(lastValue)
    if len(memory) < steps:
        for step in range(steps-1):
            memory.append(subset[step])
    
    meanMemory = np.mean(memory)
    stdMemory = np.std(memory)
    return lastValue == minValue and (lastValue < meanMemory - stdMemory)

