import numpy as np
import json
import os
import ShareAnalysisScipts.db_sqlite as sql


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
        self.data = json.dumps(data)
        self.gain = result[0]
        if len(result[1]) > 0:
            self.buyAction = json.dumps((np.array(result[1])[:,0]).tolist())
        else:
            self.buyAction = '[0]'
        if len(result[2]) > 0:
            self.sellAction = json.dumps((np.array(result[2])[:,0]).tolist())
        else:
            self.sellAction = '[0]'
        self.config = config
    
    def Save(self):
        sql.init_db()
        method_id   = sql.insert_method( (self.algorithm))
        config_id   = sql.insert_config(self.config)
        data_id     = sql.insert_data(self.data, config_id)
        result_id   = sql.insert_result((self.gain, self.buyAction, self.sellAction))
        sql.insert_cross(method_id, data_id, result_id)

    
        