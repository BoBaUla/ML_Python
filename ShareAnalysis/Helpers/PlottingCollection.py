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