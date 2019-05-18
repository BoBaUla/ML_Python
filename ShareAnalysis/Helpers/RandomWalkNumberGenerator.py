import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

class RandomWalker:

    def __init__(self, start, mu=0, sigma=1, maxStep = 0.1):
        self.Start = start
        self.Mean = mu
        self.Std = sigma
        self.MaxStep = maxStep

    def dice1(self):
        return rand.randint(40,60)

    def dice2(self):
        return rand.randint(0,100)

    def dice3(self, mu, sigma):
        return rand.normal(mu, sigma)

    def calcWalk(self,steps):
        walk = [self.Start]
        for i in range(steps):
            mu = self.Mean
            sigma = self.Std
            relStep = self.dice3(mu, sigma)
            while relStep > self.MaxStep:
                relStep = self.dice3(mu, sigma)
            last =  walk[i] 
            newStep = last + relStep
            if newStep > 0: 
                growth = np.log((newStep)/last)
            else:
                growth = np.log((newStep - (2* relStep))/last)
            if self.dice2() > self.dice1():
                walk.append(last *(1 + growth ))
            else :
                walk.append(last *(1 - growth ))
        return walk
     
    def plotNewWalk(self, steps):
        walk = [self.Start]
        for i in range(steps):
            mu = self.Mean
            sigma = self.Std
            relStep = self.dice3(mu, sigma)
            while relStep > self.MaxStep:
                relStep = self.dice3(mu, sigma)
            last =  walk[i]
            growth = np.log((last + relStep)/last)
            if self.dice2() > self.dice1():
                walk.append(last *(1 + growth ))
            else :
                walk.append(last *(1 - growth ))
        plt.plot(walk)
        plt.show()
        return walk

    def plotWalk(self, walk):
        plt.plot(walk)
        plt.show()
        
