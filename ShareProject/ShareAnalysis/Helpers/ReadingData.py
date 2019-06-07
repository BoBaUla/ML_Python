import os
import pandas as pd # lesen von csv
from Helpers.formatter import prepareData

def readData(filename, feature = 'Hoch'):
    cwd = os.getcwd()
    #folder = 'Testfiles'
    folder = 'Demofiles'
    workingfile = filename
    targetpath = os.path.join(cwd, folder, workingfile)

    csv  = pd.read_csv(targetpath,sep=';') #Achtung, das csv darf keine Leerzeilen und nicht tabellarisch relevanten Informationen enthalten 
    return prepareData(csv[feature])