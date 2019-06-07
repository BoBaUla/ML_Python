class EvaluatedData():
     def __init__(self, subset, performBuyAction, nextValue):
        self.subset = subset
        self.performBuyAction = performBuyAction
        self.nextValue = nextValue

class StratResult:
    def __init__(self, gainArray, meanGain, strategy):
        self.gainArray = gainArray
        self.meanGain = meanGain
        self.strategy = strategy