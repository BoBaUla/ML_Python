# -*- coding: utf-8 -*-
import pandas as pd 
import RelativePath as rp 

class ShareData:
    
    shareData = []

    def __init__(self, dataFile, sep = ';'):
        self.shareData = pd.read_csv(dataFile, sep = sep)        

    def GetPlainData(self, feature):
        return self.shareData[feature]
    



file = 'WireCard01.csv'
data = ShareData(rp.GetPathTo(file))
print(data.GetPlainData('Hoch'))