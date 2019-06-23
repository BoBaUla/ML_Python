import matplotlib.pyplot as plt # plotten von daten
import numpy as np 
import ShareAnalysisScipts.helper_Math as mh 
import ShareAnalysisScipts.helper_Weights as wh 
import ShareAnalysisScipts.generator_randomwalk as rw 
import ShareAnalysisScipts.plot_ScriptCollection as pc 

from ShareAnalysisScipts.config_Type import SimConfig
from ShareAnalysisScipts.eva_Performer import performStrategy
from ShareAnalysisScipts.eva_PreEvaluation_Script import preEvaluateData
from ShareAnalysisScipts.eva_Data_Mapper import StrategyMapper
from ShareAnalysisScipts.eva_Script import initLimitStrategies, filterBadStrategies, filterGoodStrategies
from ShareAnalysisScipts.eva_Data_Types import StratResult

def Run(config, evaluationStrategy):
    gainArray = []
    result = []
            
    strategies = initLimitStrategies(config.maxStrategyRange)
    mapper = StrategyMapper(config.maxStrategyRange)

    walker = rw.RandomWalker(config.init, config.mu, config.sigma)
    data = walker.calcWalk(config.dataPoints)

    for i in strategies:  
        stopLossFactor, sellAtFactor = mapper.mapNumberToStrategy(i)
        config.stopLossFactor = stopLossFactor/100
        config.sellAtFactor = sellAtFactor/100
        preparedData = preEvaluateData(data, evaluationStrategy, config.steps)
        gain = performStrategy(config, preparedData)[0]
        print(i, config.stopLossFactor, config.sellAtFactor, gain, sep = '\t')
        gainArray.append(gain)
        result.append(StratResult(gain, gain, i))

    goodStrategies = filterGoodStrategies(result, config.invest)
    badStrategies = filterBadStrategies(result, config.invest)

    avg = np.mean(gainArray)
    std = np.std(gainArray)
    mid = np.median(gainArray)
    p0 = mh.getRelationLargerThan(avg, gainArray)
    p1 = mh.getRelationLargerThan(mid, gainArray)

    fig, axs = plt.subplots(2,3)

    print('WSK: ' + str(p0 * 100),'Ctl: ' + str(p1*100) ,'AVG: ' + str(avg),'MID: ' +str(mid),'STD: ' + str(std), sep = '\n')
    
    pc.plotData(axs[0][0], data, 'data')
    axs[0][0].grid()

    pc.plotData(axs[1][0],gainArray, 'strat results')
    axs[1][0].grid()

    pc.plotHist(goodStrategies[0], axs[1][1], 1,  color = 'green', title='positive strats')
    pc.plotHist(goodStrategies[1], axs[1][2], 5,  color = 'green', title='positive results')

    pc.plotHist(badStrategies[0], axs[0][1], 1, color= 'red', title='negative strats')
    pc.plotHist(badStrategies[1], axs[0][2], 5, color= 'red', title='negative results')
    plt.show()

