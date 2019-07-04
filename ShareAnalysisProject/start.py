from ShareAnalysisScipts.config_Type import TradeConfig, WalkerConfig
import ShareAnalysisScipts.eva_PreEvaluationStrategies as strategy
import numpy as np
from ShareAnalysisScipts import  sim_OneWalkManySellingStrategies, sim_OneWalkOneBuyStrategy, sim_OneWalkDifferentBuyingStrategies, sim_ManyWalksOneSellingStrategy

configTrade = TradeConfig(
    invest = 10000,
    fee = 5,
    sellAtFactor = 5,
    stopLossFactor = 5,
    maxStrategyRange = 5,
    steps = 50
)

congWalker = WalkerConfig(
    dataPoints = 1000,
    mu = np.random.randint(1,100),
    sigma = np.random.randint(1,5)
    )


# sim_ManyWalksOneSellingStrategy.Run(configTrade = configTrade, configWalker = congWalker, simulations = 10, evaluationStrategy = strategy.buyAtLocalMinimum_Evaluation, save=True)
# sim_OneWalkManySellingStrategies.Run(configTrade = configTrade, configWalker = congWalker, evaluationStrategy = strategy.buyAtLocalMinimumWithReset_Evaluation, save = True)

strategies = [strategy.buyAtLocalMinimumWithReset_Evaluation, strategy.startIntervallEvaluation, strategy.squareInterpolation_HasMaximumEvaluation]
sim_OneWalkOneBuyStrategy.Run(configTrade = configTrade, configWalker = congWalker, evaluationStrategies = strategies, save= True)
# sim_OneWalkDifferentBuyingStrategies.Rusn(configTrade = configTrade, configWalker = congWalker)