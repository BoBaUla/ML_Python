class Offer():

    def __init__(self, price, volume):
        self.Price = price
        self.Volume = volume

class Trade():
    
    def __init__(self, price, volumeSell, volumeBuy):
        self.Price = price
        self.VolumeSell = volumeSell
        self.VolumeBuy = volumeBuy

    def getTradeVolume(self):
        return self.Price * min(self.VolumeBuy, self.VolumeSell)

def getPrices(offers):
    prices = []
    for offer in offers:
        if not prices.__contains__(offer.Price):
            prices.append(offer.Price)
    prices.sort()
    return prices

def getPossiblePurchasVolume(price, offers):
    """Zählt die Anteile der Marktteilnehmer die zu gegebenen Preis einkaufen würden"""
    volume = 0
    for offer in offers:
        if price <= offer.Price:
            volume = volume + offer.Volume
    return volume

def getPossibleSaleVolume(price, offers):
    """Zählt die Anteile der Marktteilnehmer die zu gegebenen Preis verkaufen würden"""
    volume = 0
    for offer in offers:
        if price >= offer.Price:
            volume = volume + offer.Volume
    return volume

def getPossibleTrades(possiblePrices, sellOrders, buyOrders):
    possibleTrades = []
    for price in possiblePrices:
        possibleTrades.append(
            Trade(
                price, 
                getPossibleSaleVolume(price, sellOrders),
                getPossiblePurchasVolume(price, buyOrders)))
    return possibleTrades

def getBestTrade(possibleTrades):
    return max(possibleTrades, key = lambda a: a.getTradeVolume())

def computeTrade(sellOrder, buyOrder):
    pricesSell = getPrices(sellOrder)
    pricesBuy = getPrices(buyOrder)
    possiblePrices = [value for value in pricesSell if value in pricesBuy]
    possibleTrades = getPossibleTrades(possiblePrices, sellOrder, buyOrder)
    bestTrade = getBestTrade(possibleTrades)
    
    return bestTrade

# sellOrder = [Offer(10,1), Offer(9,2), Offer(8,3), Offer(10,3)]  #Verkauf
# buyOrder = [Offer(7,5), Offer(8,3), Offer(9,2), Offer(10,1)]    #Einkauf

# print(getPossiblePurchasVolume(8, buyOrder))
# result = getPossibleTrades([8], sellOrder, buyOrder)
# print(result)