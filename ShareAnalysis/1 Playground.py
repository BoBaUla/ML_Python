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
windowSize = 20
fig, axs = plt.subplots(2,2)

rw = RW(10, mu_0, sigma)

data = rw.calcWalk(steps)
mu_data = np.mean(data)
stabw_data = np.std(data)
plotData(axs[0][0], 'mu_subset', data)
plotData(axs[1][0], 'mu_subgrowth', data)

growth = relativeGrowth(data)
mu_growth = np.mean(growth)
stabw_growth = np.std(growth)

mu_toPlot =[]
i_toPlot = []
subsetToPlot = []
for i in range(len(data)-windowSize):
    subset = getSubset(data, i, windowSize)
    mu_subset = np.mean(subset)
    stabw_subset = np.std(subset)
    mu_toPlot.append( mu_subset)
    i_toPlot.append(i+windowSize)

    data_0_to_i = getSubset(data,0,i+windowSize)
    mu_data_0_to_i = np.mean(data_0_to_i)
    if mu_data_0_to_i < mu_subset:
        subsetToPlot.append([subset, i])
        
for subset in subsetToPlot:
        plotData(axs[0][0], 'mu_subset', [], [getXValues(subset[1]),subset[0]])

plotData(axs[0][0],'mean', [], [i_toPlot, mu_toPlot], subdataColor = 'r--')
# plotData(axs[0][0],'mean', [], mu_toPlot, dataColor = 'r--')

mu_toPlot =[]
subsetToPlot = []
for i in range(len(data)-windowSize-1):
    subset = relativeGrowth(getSubset(data, i, windowSize))
    mu_subset = np.mean(subset)
    stabw_subset = np.std(subset)
    mu_toPlot.append(mu_subset)
        
    data_0_to_i = relativeGrowth(getSubset(data,0,i+windowSize))
    mu_data_0_to_i = np.mean(data_0_to_i)
    if mu_data_0_to_i < mu_subset:
        subsetToPlot.append([getSubset(data, i, windowSize), i])

for subset in subsetToPlot:
        plotData(axs[1][0], 'mu_subgrowth', [], [getXValues(subset[1]),subset[0]])

plotData(axs[1][1],'mu_subgrowth', mu_toPlot, dataColor = 'r.')
plt.show()


