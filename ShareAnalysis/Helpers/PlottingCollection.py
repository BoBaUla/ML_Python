import numpy as np

def filterZero(data):
        result = []
        for dat in data:
                if dat > 0:
                        result.append(dat)
        return result


def plotHist(data, plt, step, color = 'blue', title =''):
        if len(data) == 0:
                return 

        bins = np.arange(min(data), max(data)+2, step)
        val = plt.hist(data, bins= bins, color = color)
        valY = val[0]
        valX = val[1]
        avg = np.mean(filterZero(valY))
        std = np.std(filterZero(valY))
        plt.plot([min(valX), max(valX)],[avg,avg], 'r-')
        plt.plot([min(valX), max(valX)],[avg+std,avg+std], 'g-')
        plt.set_title(title)
        plt.grid()
        return valX, valY, avg, std

def plotResults(plt, description, data, results, logging = True):
    plt.plot(data, 'k-')
    plt.set_title(description)

    if len(results[1]) > 0:
        buyX = np.array(results[1])[:,0]
        buyY = np.array(results[1])[:,1]
        plt.plot(buyX, buyY, 'go', label = 'buy')

    if len(results[2]) > 0:
        sellX = np.array(results[2])[:,0]
        sellY = np.array(results[2])[:,1]
        plt.plot(sellX, sellY, 'rx', label = 'sell')
    plt.legend()
    plt.grid()

    if logging:
        print(description, results[0], sep= '\t')

def plotData(plt, description, data, subdata = [], subdataColor='g-'):
    plt.plot(data, 'k-')
    if len(description) >0:
        plt.set_title(description)
        
    if len(subdata) > 0:
        plt.plot(subdata[0], subdata[1], subdataColor, label = 'subset')
