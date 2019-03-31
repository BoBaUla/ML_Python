import os

cwd = os.getcwd()
relativePath = '..'
directory = 'Demofiles'

def GetPathTo(file):
    path = os.path.join( relativePath, directory, file)
    return os.path.join(cwd,path)