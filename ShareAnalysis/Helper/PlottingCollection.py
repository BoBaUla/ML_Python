import numpy as np

def plottDataLayout(data, plt, plottingString = 'k-', label = '', showGrid = True, xLineLabel = '', showXLine = False, showXLineAt = 0, title ='', xlabel = 'x Achse', ylabel = 'y Achse', xlen = 0):
    plt.grid(which='minor', alpha=0.2)
    plt.grid(which='major', alpha=0.5)     
     
    if showXLine:
        minValue = 0
        maxValue = xlen
        plt.plot([minValue, maxValue],[showXLineAt,showXLineAt], 'k-', label = xLineLabel)    

    plt.plot(data, plottingString, label =label)

    plt.set_title(title)
    plt.set_xlabel(xlabel)
    plt.set_ylabel(ylabel)
    plt.legend()      
    return plt

def plotHistogram(
    data, plt, label='', rwidth=1, 
    title='', xlabel = '', ylabel = '', 
    stepsize = 20):
    maxData = max(data)
    minData = min(data)
    gridSize = maxData - minData
    delta = gridSize / stepsize
    binRange = np.arange(minData, maxData, delta)
    plt.hist(data, label = label, rwidth = rwidth, bins = binRange )
    plt.set_title(title)
    plt.set_xlabel(xlabel)
    plt.set_ylabel(ylabel)
    plt.grid()
    plt.legend()


def plottKorellation(
    data, plt, plottingString = 'k-', label = '', 
    showGrid = True, title ='', xlabel = 'x Achse', ylabel = 'y Achse'):
    minValueX = round(min(data[0]),2)
    maxValueX = round(max(data[0]),2)
    minValueY = round(min(data[1]),2)
    maxValueY = round(max(data[1]),2)
    
    if showGrid:
       
        maxDeltaX = (maxValueX-minValueX)/10
        major_ticks_X = np.arange(minValueX, maxValueX, maxDeltaX )
        minor_ticks_X = np.arange(minValueX, maxValueX, maxDeltaX/10)

        maxDeltaY = (maxValueY-minValueY)/10
        major_ticks_Y = np.arange(minValueY - maxDeltaY, maxValueY + maxDeltaY, maxDeltaY )
        minor_ticks_Y = np.arange(minValueY- maxDeltaY, maxValueY + maxDeltaY, maxDeltaY/10)

        plt.set_xticks(major_ticks_X)
        plt.set_xticks(minor_ticks_X, minor=True)
        plt.set_yticks(major_ticks_Y)
        plt.set_yticks(minor_ticks_Y, minor=True)
        plt.grid(which='both')
        # Or if you want different settings for the grids:
        plt.grid(which='minor', alpha=0.2)
        plt.grid(which='major', alpha=0.5)     
     
    plt.plot([minValueX, maxValueX], [0,0], 'k-')    
    plt.plot([0,0], [minValueY, maxValueY], 'k-')    

    plt.plot(data[0],data[1], plottingString, label =label)

    plt.set_title(title)
    plt.set_xlabel(xlabel)
    plt.set_ylabel(ylabel)
    
    plt.legend()      
    return plt

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def test_answer2():
    assert func(3) == 6