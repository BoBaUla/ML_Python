import numpy as np 

class SimConfig(object):

    def __init__(
        self, 
        dataPoints = 2000, 
        invest = 1000, 
        fee = 5, 
        steps = 100, 
        init = np.random.randint(50,150), 
        mu = 0, 
        sigma = 0.4, 
        sellAtFactor = 0.08, 
        stopLossFactor = 0.08,
        maxGainFactor = 0.2):

        self.dataPoints = dataPoints
        self.invest = invest
        self.fee = fee
        self.steps = steps
        self.init = init
        self.mu = mu
        self.sigma = sigma
        self.sellAtFactor = sellAtFactor
        self.stopLossFactor = stopLossFactor
        self.maxGainFactor = maxGainFactor