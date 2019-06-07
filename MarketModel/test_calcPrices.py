from calcPrice import *
import pytest

sellOrder = [Offer(10,1), Offer(9,2), Offer(8,3), Offer(10,3), Offer(11,2)]  #Verkauf
buyOrder = [Offer(7,5), Offer(8,3), Offer(9,2), Offer(10,1)]    #Einkauf
# pytest test_calcPrices.py
class TestCalcPrice(object):

    def test_getsPrices(self):
        result = getPrices(sellOrder)
        expectedResult = [8,9,10,11]

        assert result == expectedResult

    def test_getPossiblePurchases(self):
        result = getPossiblePurchasVolume(8, buyOrder)
        expectedResult = buyOrder[1].Volume + buyOrder[2].Volume + buyOrder[3].Volume

        assert result == expectedResult
        
    def test_getPossibleSales(self):
        result = getPossibleSaleVolume(9, sellOrder)
        expectedResult = sellOrder[1].Volume + sellOrder[2].Volume

        assert result == expectedResult

    def test_getPossibleTrade(self):
        results = getPossibleTrades([8], sellOrder, buyOrder)
        expectedResults = [Trade(8,3,6)]
        
        for i in range(len(results)):
            assert results[i].Price == expectedResults[i].Price
            assert results[i].VolumeBuy == expectedResults[i].VolumeBuy
            assert results[i].VolumeSell == expectedResults[i].VolumeSell

    def test_getPossibleTrades(self):
        results = getPossibleTrades([8,9,10], sellOrder, buyOrder)
        expectedResults = [Trade(8,3,6),Trade(9,5,3),Trade(10,9,1)]
        
        for i in range(len(results)):
            assert results[i].Price == expectedResults[i].Price
            assert results[i].VolumeBuy == expectedResults[i].VolumeBuy
            assert results[i].VolumeSell == expectedResults[i].VolumeSell

    def test_getBestTrade(self):
        result = getBestTrade([Trade(1,1,1), Trade(2,2,1), Trade(10,2,3)])
        
        assert result.Price == 10
        assert result.VolumeBuy == 3
        assert result.VolumeSell == 2


    def test_computeTrade(self):
        result = computeTrade(sellOrder, buyOrder)
        expectedResult = Trade(9,5,3)
        
        assert result.Price == expectedResult.Price
        assert result.VolumeBuy == expectedResult.VolumeBuy
        assert result.VolumeSell == expectedResult.VolumeSell
        assert result.getTradeVolume() == 27