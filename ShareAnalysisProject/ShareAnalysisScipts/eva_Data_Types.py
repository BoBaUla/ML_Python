import numpy as np
import json
import os

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


class EvaluationResult():
    def __init__(self, data, result, config, algorithm):
        self.algorithm = algorithm
        self.data = data
        self.gain = result[0]
        if len(result[1]) > 0:
            self.buyAction = json.dumps((np.array(result[1])[:,0]).tolist())
        else:
            self.buyAction = []
        if len(result[2]) > 0:
            self.sellAction = json.dumps((np.array(result[2])[:,0]).tolist())
        else:
            self.sellAction = []
        self.config = json.dumps(config.__dict__)
    
    def Save(self):
        cwd = os.getcwd()
        target = os.path.join(cwd, self.algorithm)
        # name = 
        if not(self.algorithm in os.listdir(target)):
            os.mkdir()
        
        return json.dumps(self.__dict__)


    
        