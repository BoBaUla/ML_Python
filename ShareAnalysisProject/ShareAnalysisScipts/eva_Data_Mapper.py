class StrategyMapper():

    maxRange = 1

    def __init__(self, maxStrategyRange):
        self.maxStrategyRange = maxStrategyRange


    def mapStategyToNumber(self, strat):
        return strat[0]* self.maxStrategyRange + strat[1]

    def mapNumberToStrategy(self, strat):
        sellAt = strat % self.maxStrategyRange
        stopLoss = int((strat - sellAt) / self.maxStrategyRange)
        return [stopLoss, sellAt]