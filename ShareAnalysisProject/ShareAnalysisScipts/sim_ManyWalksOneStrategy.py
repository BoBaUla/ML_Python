import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import ShareAnalysisScipts.plot_ScriptCollection as pc 
import ShareAnalysisScipts.helper_Math as mh 
import ShareAnalysisScipts.helper_Weights as wh 
import ShareAnalysisScipts.generator_randomwalk as rw 

from ShareAnalysisScipts.eva_Performer import performStrategy

from ShareAnalysisScipts.eva_PreEvaluation_Script import preEvaluateData

def Run(config, simulations, evaluationStrategy):
    gainArray = []
  
    for i in range(simulations):
        walker = rw.RandomWalker(config.init, config.mu, config.sigma, 0.2)
        data = walker.calcWalk(config.dataPoints)
        preparedData = preEvaluateData(data, evaluationStrategy, config.steps)
        gainArray.append(performStrategy(config, preparedData)[0])

    avg = np.mean(gainArray)
    std = np.std(gainArray)
    mid = np.median(gainArray)
    p0 = mh.getRelationLargerThan(avg, gainArray)
    p1 = mh.getRelationLargerThan(mid, gainArray)

    print('WSK: ' + str(p0 * 100),'Ctl: ' + str(p1*100) ,'AVG: ' + str(avg),'MID: ' +str(mid),'STD: ' + str(std), sep = '\n')
    plt.plot(gainArray)
    plt.grid()
    plt.show()

