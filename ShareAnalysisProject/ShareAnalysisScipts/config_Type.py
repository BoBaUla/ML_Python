import numpy as np 
import hashlib

class SimConfig(object):

    def __init__(
        self, 
        dataPoints = 2000, #Anzahl der Werte im Randomwalk
        invest = 1000,  #Startkapital
        fee = 5, #Ordergebühren
        steps = 100, #Länge des für Orderentscheidungen zu untersuchenden Intervalls
        init = np.random.randint(50,150), #Startpunkt des Randomwalks
        mu =  np.random.randint(0,100), # Peak der glockenkurve
        sigma =  np.random.randint(0,10), # Wendepunkte der Glockenkurve 1-sigma, 2-sigma 3-sigma Intervalle
        sellAtFactor = 8, # Faktor ab dem der Gewinn verkauft werden soll
        stopLossFactor = 8, # Faktor der maximalen Verlust einer Aktion modelliert
        maxGainFactor = 20, # Faktor der den maximalen Gesamtgewinn beschreibt
        maxStrategyRange = 10): # Anzahl aller möglichen sellAt/stopLoss Faktoren (wird quadratisch betrachtet)

        self.dataPoints = dataPoints
        self.invest = invest
        self.fee = fee
        self.steps = steps
        self.init = init
        self.mu = mu / 100
        self.sigma = sigma / 100
        self.sellAtFactor = sellAtFactor / 100
        self.stopLossFactor = stopLossFactor / 100
        self.maxGainFactor = maxGainFactor / 100
        self.maxStrategyRange = maxStrategyRange
    
    def ConfigID(self):
        
        val = (str(self.dataPoints)+str(self.invest)+str(self.fee)+str(self.init)+str(self.mu*100)+str(self.sigma*100)+str(self.sellAtFactor*100)+str(self.stopLossFactor*100)+str(self.maxGainFactor*100)+str(self.maxStrategyRange)).replace('.','')
        return int(val)
