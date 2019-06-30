from ShareAnalysisScipts.config_Type import SimConfig
import ShareAnalysisScipts.eva_PreEvaluationStrategies as strategy
import numpy as np
from ShareAnalysisScipts import  sim_OneWalkManySellingStrategies, sim_OneWalkOneBuyStrategy, sim_OneWalkDifferentBuyingStrategies, sim_ManyWalksOneSellingStrategy

config = SimConfig(
    invest = 10000,
    fee = 5,
    init = 100,    
    dataPoints = 20,
    mu = np.random.randint(1,100),
    sigma = np.random.randint(1,5),
    sellAtFactor = 5,
    stopLossFactor = 5,
    maxStrategyRange = 10,
    steps = 5
)

sim_ManyWalksOneSellingStrategy.Run(config = config, simulations = 10, evaluationStrategy = strategy.buyAtLocalMinimum_Evaluation)
# sim_OneWalkManySellingStrategies.Run(config = config, evaluationStrategy = strategy.buyAtLocalMinimumWithReset_Evaluation)
sim_OneWalkOneBuyStrategy.Run(config = config, evaluationStrategies = [strategy.buyAtLocalMinimumWithReset_Evaluation, strategy.buyAtLocalMinimumWithReset_Evaluation])
# sim_OneWalkDifferentBuyingStrategies.Run(config = config)