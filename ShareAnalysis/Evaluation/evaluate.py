import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import Helpers.PlottingCollection as pc 
import Helpers.mathHelper as mh
from Helpers.ReadingData import readData
from Evaluation.PreEvaluation import preEvaluateData
from Evaluation.Performer import performStrategy

workingfiles = [
    'SAP_05_04_19_Intraday.csv',
'SAP_03_04_bis_05_04_Week.csv',
'SAP_2019-03-25_bis_2019-04-05_2Week.csv',
'SAP_2019-01-07_bis_2019-04-05_3Month.csv',
'SAP_2018-10-08_bis_2019-04-05_6Month.csv',
'SAP_2018-04-09_bis_2019-04-05_Year.csv',
'SAP_2014-04-11_bis_2019-04-05_5Years.csv']

steps = 50
limitU = 0.09
limitD = 0.01
fee = 5
for i in workingfiles:
    data =  readData(i)
    prepateredData = preEvaluateData(data, steps= steps)
    [gain, buy, sell] = performStrategy(10000, fee, prepateredData, data, steps, limitU, limitD)
    if len(buy) >0 and len(sell)>0:
        buyX = np.array(buy)[:,0]
        buyY = np.array(buy)[:,1]

        sellX = np.array(sell)[:,0]
        sellY = np.array(sell)[:,1]


        fig, axs = plt.subplots(2,1)
        fig.title = i
        axs[0].plot(data, 'k-')
        axs[0].plot(buyX, buyY, 'go', label = 'buy')
        axs[0].plot(sellX, sellY, 'rx', label = 'sell')

        d = mh.returnFromData(data)
        axs[1].plot(d, 'k-')
        axs[0].legend()      
        print(gain)
        plt.show()
