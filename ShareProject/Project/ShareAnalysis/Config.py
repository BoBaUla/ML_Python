import numpy as np 

class SimConfig(object):

    def __init__(
        self, 
        dataPoints = 2000, #Anzahl der Werte im Randomwalk
        invest = 1000,  #Startkapital
        fee = 5, #Ordergebühren
        steps = 100, #Länge des für Orderentscheidungen zu untersuchenden Intervalls
        init = np.random.randint(50,150), #Startpunkt des Randomwalks
        mu = 0, # Peak der glockenkurve
        sigma = 0.4, # Wendepunkte der Glockenkurve 1-sigma, 2-sigma 3-sigma Intervalle
        sellAtFactor = 0.08, # Faktor ab dem der Gewinn verkauft werden soll
        stopLossFactor = 0.08, # Faktor der maximalen Verlust einer Aktion modelliert
        maxGainFactor = 0.2, # Faktor der den maximalen Gesamtgewinn beschreibt
        maxStrategyRange = 10): # Anzahl aller möglichen sellAt/stopLoss Faktoren (wird quadratisch betrachtet)

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
        self.maxStrategyRange = maxStrategyRange