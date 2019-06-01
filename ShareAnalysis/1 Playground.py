from Helpers.RandomWalkNumberGenerator import RandomWalker as RW
from Helpers.PlottingCollection import plotData
from Helpers.mathHelper import returnFromDataRelativ as relativeGrowth
from Evaluation.PreEvaluation import getSubset
import matplotlib.pyplot as plt
import numpy as np 

def getXValues(i):
    return range(i, i + windowSize)

mu_0 = 2
sigma = 1
steps = 1000
windowSize = 500
fig, axs = plt.subplots(2)

rw = RW(10, mu_0, sigma)

data = rw.calcWalk(steps)
mu_data = np.mean(data)
stabw_data = np.std(data)

growth = relativeGrowth(data)
mu_growth = np.mean(growth)
stabw_growth = np.std(growth)

subsetToPlot = []
mu_toPlot = 0
index = 0
for i in range(len(data)-windowSize):
    subset = getSubset(data, i, windowSize)
    mu_subset = np.mean(subset)
    stabw_subset = np.std(subset)
    if mu_toPlot < mu_subset and mu_data < mu_subset:
        subsetToPlot = subset
        mu_toPlot = mu_subset
        index = i
        print(i, mu_subset, mu_toPlot, sep = '\t')

plotData(axs[0], ' ', data, [getXValues(index),subsetToPlot])

plt.show()


