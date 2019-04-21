def changeDirection(stringList):
    values = []
    for i in range(len(stringList)):
        length = len(stringList)
        values.append(stringList[length -1 -i])
    return values

def makeFloatList(stringList, decimalPoint = ','):
    floatList = []
    for i in stringList:
        floatList.append(float(i.replace(decimalPoint,'.')))
    return floatList

def prepareData(dataList):
    redirect = changeDirection(dataList)
    return makeFloatList(redirect)