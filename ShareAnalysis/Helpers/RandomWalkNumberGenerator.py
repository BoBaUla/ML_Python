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

    def dice3(self):
        value = rand.normal(self.Mean, self.Std)
        if value > self.MaxStep:
            value = self.MaxStep
        if value < (-1)*self.MaxStep:
            value = (-1)*self.MaxStep
        return value

    def getRelativeChange(self, dice3):
        return 1 + dice3(self) / 100

    def calcWalk(self,steps, dice1 = dice1, dice2 = dice2, dice3 = dice3):
        walk = [self.Start]
        for i in range(steps):
            relativeChange = self.getRelativeChange(dice3)
            last =  walk[i] 
            if dice2(self) > dice1(self):
                walk.append(last * relativeChange)
            else :
                walk.append(last / relativeChange)
        return walk
     
    def plotNewWalk(self, steps, dice1 = dice1, dice2 = dice2, dice3 = dice3):
        walk = self.calcWalk(steps)
        plt.plot(walk)
        plt.show()
        return walk

    def plotWalk(self, walk):
        plt.plot(walk)
        plt.show()
        
# walker = RandomWalker(1)
# walker.plotNewWalk(10000)