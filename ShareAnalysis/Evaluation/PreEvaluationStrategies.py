from Helpers.WeightsHelper import ExpectedValue
from Helpers.mathHelper import linearInterpolation, squareInterpolation

def lastValue(subset, steps):
    return subset[steps - 1]

def evaluateByFallingSituation(subset, steps):
    return ExpectedValue(subset,1) > lastValue(subset, steps)

def evaluateByRisingSituation(subset, steps):
    return ExpectedValue(subset,1) < lastValue(subset, steps)

def endIntervallEvaluation(subset, steps = 1):
    return subset[0] < lastValue(subset, steps)

def startIntervallEvaluation(subset, steps = 1):
    return subset[0] > lastValue(subset, steps)

def linearInterpolationRisingEvaluation(subset, steps = 1):
    return linearInterpolation(subset)[0] > 0

def linearInterpolationFallingEvaluation(subset, steps = 1):
    return linearInterpolation(subset)[0] < 0

def squareInterpolation_HasMinimumEvaluation(subset, steps = 1):
    return squareInterpolation(subset)[0] > 0

def squareInterpolation_HasMaximumEvaluation(subset, steps = 1):
    return squareInterpolation(subset)[0] < 0
