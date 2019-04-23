import numpy as np 

def sellStrategy(price, sellAt, stopLoss):
    return (price > sellAt or price <= stopLoss)

def buyStrategy(buy, canBuy, money, cost, price):
    return buy and money - cost > price and canBuy

def performStrategy(money, cost, evaluatedData, dataSrc, steps, 
    limitFactor = 0, stopLossFactor = 0, 
    sellStrategy = sellStrategy, buyStrategy = buyStrategy):    
    # print('evaluateData')
    price = 0
    money = money
    evaluatedData = evaluatedData
    dataSrc = dataSrc
    steps = steps
    share = 0
    sellAt = 0
    stopLoss = 0
    buyAction = []
    sellAction = []
    dataNr = 0
    for dataset in evaluatedData:
        buy = dataset[steps]
        index = dataNr + steps
        price = dataSrc[index]
        canBuy = True

        if share > 0:
            if sellStrategy(price, sellAt, stopLoss):
                money = round((money + price * share) - cost,2)
                share = 0
                canBuy = False
                sellAction.append(np.array([index, price, share, money]))
                # print('i', stopLossFactor, 'j', limitFactor,'sell', 
                # 'dataNr', dataNr , round(price,2), round(sellAt,2), round(stopLoss,2), sep = '\t')

        if buyStrategy(buy, canBuy, money, cost, price):
            share = int((money - cost)/price) + share
            money = round(money - share * price - cost,2)
            sellAt = price * (1 + limitFactor)
            stopLoss = price * (1 -stopLossFactor)
            buyAction.append(np.array([index, price, share, money]))
            # print('i', stopLossFactor, 'j', limitFactor,'buy',
            # 'dataNr', dataNr , round(price,2), round(sellAt,2), round(stopLoss,2), sep = '\t')
        dataNr = dataNr + 1
        #print(i, round(price,2), sep='\t')
    gain = round(money + share * price,2)
    return gain, buyAction, sellAction 