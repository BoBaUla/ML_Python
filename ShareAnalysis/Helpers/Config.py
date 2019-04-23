import numpy as np 

class SimConfig(object):

    def __init__(self, dataPoints = 2000, invest = 1000, fee = 5, steps = 100, init = np.random.randint(50,150), mu = 0, sigma = 0.4, sellAtFactor = 0.08, stopLossFactor = 0.08):
        self.dataPoints = 2000
        self.invest = 1000   
        self.fee = 5
        self.steps = 100
        self.init = np.random.randint(50,150)
        self.mu = 0
        self.sigma = 0.4
        self.sellAtFactor = 0.08
        self.stopLossFactor = 0.08