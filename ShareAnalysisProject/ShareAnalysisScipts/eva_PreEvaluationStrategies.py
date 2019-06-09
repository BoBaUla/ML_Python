from ShareAnalysisScipts.helper_Weights import ExpectedValue
from ShareAnalysisScipts.helper_Math import linearInterpolation, squareInterpolation
import ShareAnalysisScipts.eva_Memory as mem
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

def buyAtLocalMinimum_Evaluation(subset):
    minValue = min(subset)
    lastValue = getLastValue(subset)    
    
    mem.setMemory(lastValue)
    
    meanMemory = np.mean(mem.memory)
    stdMemory = np.std(mem.memory)
    result = lastValue == minValue and (lastValue < meanMemory - stdMemory)
    
    return result

def buyAtLocalMinimumWithReset_Evaluation(subset):
    minValue = min(subset)
    steps = len(subset)
    lastValue = getLastValue(subset)
    
    if len(mem.memory) >= steps *3:
        mem.resetMemory()

    mem.setMemory(lastValue)
    
    meanMemory = np.mean(mem.memory)
    stdMemory = np.std(mem.memory)
    result = lastValue == minValue and (lastValue < meanMemory - stdMemory)
    
    return result

