import numpy as np 
from config_Type import SimConfig

def sellStrategy(price, sellAt, stopLoss):
    return (price > sellAt or price <= stopLoss)

def enoughMoneyLeft(money, cost, price):
    return money - cost > price

def buyShare(money, fee, price, share):
    return int((money - fee)/price) + share

def adjustMoneyAfterBuyAction(money, fee, price, share):
    return round(money - share * price - fee,2)

def getLastPrice(evaluatedData, steps):
    return evaluatedData[len(evaluatedData)- 1].subset[steps - 1]
    

def performStrategy(config, evaluatedData, sellStrategy = sellStrategy):    
    # print('evaluateData')
    if  not (isinstance(config, SimConfig)):
        return 0, [], []

    price = 0
    money = config.invest
    maxGain = config.invest * (1+config.maxGainFactor)
    steps = config.steps
    fee = config.fee
    limitFactor = config.sellAtFactor
    stopLossFactor = config.stopLossFactor

    evaluatedData = evaluatedData

    share = 0
    sellAt = 0
    stopLoss = 0
    buyAction = []
    sellAction = []
    dataNr = 0
    for dataset in evaluatedData:
        buy = dataset.performBuyAction
        price = dataset.nextValue
        index = dataNr + steps
        if money >= maxGain:
            break

        if buy and enoughMoneyLeft(money, fee, price) and price > 0:
            share = buyShare(money, fee, price, share)
            money = adjustMoneyAfterBuyAction(money, fee, price, share)
            sellAt = price * (1 + limitFactor)
            stopLoss = price * (1 - stopLossFactor)
            buyAction.append(np.array([index, price, share, money]))
            # print('i', stopLossFactor, 'j', limitFactor,'buy',
            # 'dataNr', dataNr , round(price,2), round(sellAt,2), round(stopLoss,2), sep = '\t')
        elif share > 0 and sellStrategy(price, sellAt, stopLoss) and price > 0:
            money = round((money + price * share) - fee,2)
            share = 0
            sellAction.append(np.array([index, price, share, money]))
            # print('i', stopLossFactor, 'j', limitFactor,'sell', 
            # 'dataNr', dataNr , round(price,2), round(sellAt,2), round(stopLoss,2), sep = '\t')

        dataNr = dataNr + 1
        #print(i, round(price,2), sep='\t')
    
    gain = round(money + share * getLastPrice(evaluatedData, steps),2)
    return gain, buyAction, sellAction 