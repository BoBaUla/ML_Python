import Helper.mathHelper as mh 
import numpy as np 
import matplotlib.pyplot as plt # plotten von daten

def generateWeights(dataYield):
    prop = mh.getBinomialPropability(dataYield)
    antiprop = 1 - prop
    result = []
    for value in dataYield:
        if value > 0:
            result.append(prop)
        else:
            result.append(antiprop)
    return result

def adjustAVG(data, a0, w0, avg):
    N = len(data)
    aNext = data[N-1]
    temp0 = np.log(aNext/data[N-2])
    temp1 = np.log(data[0]/a0)
    if temp0 * temp1 > 0:
        return data[0], w0, (avg - a0*w0/N + aNext*w0/N)
    else:
        growth = mh.returnFromData(data)
        growth[2:N].append(temp0)
        weights = generateWeights(growth)
        return data[0], weights[0], np.average(data[1:N], weights=weights)
    
def initAVG(data, steps):
    initialSubset = data[0: steps]
    a0 = initialSubset[0]
    initialGrowth = mh.returnFromData(initialSubset)
    initialWeights = generateWeights(initialGrowth)
    initialAvg = np.average(initialSubset[1:steps], weights=initialWeights)
    return a0, initialWeights[0], initialAvg

def preEvaluateData(data, steps = 1):
    # print('preEvaluateData')
    if steps == 0:
        return []
    evaluatedData = []
    lastIndex = len(data)- steps - 1
    a0, w0, avg = initAVG(data, steps)    
    for i in range(lastIndex):
        subset = data[i: i+steps]    
        a0, w0, avg = adjustAVG(subset, a0, w0, avg )
        buy = (subset[steps-1] > avg)
        # prop = mh.getPropability(mh.yieldFromData(subset))
        # buy = (prop > 0.5)
        

        evaluation = [buy]
        subset.append(evaluation)
        evaluatedData.append(subset)
    return evaluatedData

def evaluateData(money, cost, evaluatedData, dataSrc, steps, limitFactor = 0, stopLossFactor = 0):    
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
        evaluation = dataset[steps]
        buy = evaluation[0]
        index = dataNr + steps
        price = dataSrc[index]
        canBuy = True

        if share > 0:
            if (price > sellAt or price <= stopLoss):
                money = round((money + price * share) - cost,2)
                share = 0
                canBuy = False
                sellAction.append(np.array([index, price, share, money]))
                # print('i', stopLossFactor, 'j', limitFactor,'sell', 
                # 'dataNr', dataNr , round(price,2), round(sellAt,2), round(stopLoss,2), sep = '\t')

        if buy and money - cost > price and canBuy:
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
   