from ShareAnalysisScipts.config_Type import TradeConfig
import ShareAnalysisScipts.eva_PreEvaluationStrategies as strategy
import numpy as np
from ShareAnalysisScipts import  sim_OneWalkManySellingStrategies, sim_OneWalkOneBuyStrategy, sim_OneWalkDifferentBuyingStrategies, sim_ManyWalksOneSellingStrategy

config = TradeConfig(
    invest = 10000,
    fee = 5,
    init = 100,    
    dataPoints = 1000,
    mu = np.random.randint(1,100),
    sigma = np.random.randint(1,5),
    sellAtFactor = 5,
    stopLossFactor = 5,
    maxStrategyRange = 5,
    steps = 50
)

# sim_ManyWalksOneSellingStrategy.Run(config = config, simulations = 10, evaluationStrategy = strategy.buyAtLocalMinimum_Evaluation, save=True)
# sim_OneWalkManySellingStrategies.Run(config = config, evaluationStrategy = strategy.buyAtLocalMinimumWithReset_Evaluation, save = True)

strategies = [strategy.buyAtLocalMinimumWithReset_Evaluation, strategy.startIntervallEvaluation, strategy.squareInterpolation_HasMaximumEvaluation]
sim_OneWalkOneBuyStrategy.Run(config = config, evaluationStrategies = strategies, save= True)
# sim_OneWalkDifferentBuyingStrategies.Rusn(config = config)