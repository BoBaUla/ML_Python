import numpy as np 

memory = []
meanMemory = []
stdMemory = []

def adjustMeanMemory():
    mean = np.mean(memory)
    meanMemory.append(mean)

def adjustStdMemory():
    std = np.std(memory)
    stdMemory.append(std)

def setMemory(lastValue):
        memory.append(lastValue)
        adjustMeanMemory()
        adjustStdMemory()

def resetMemory():
    memory.clear()

def resetMeanMemory():
    meanMemory.clear()

def resetStdMemory():
    stdMemory.clear()

def resetAll():
        resetMeanMemory()
        resetMemory()
        resetStdMemory()