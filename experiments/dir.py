import os

# string subtract
def str_subtract(s1, s2):
    for ch in s2:
        if ch in s1:
            s1 = s1.replace(ch, '', 1)
    return s1



# get name of the current directory
def getDir():
    s1 = os.getcwd()
    s2 = os.path.dirname(s1)
    dir = str_subtract(s1, s2)
    dir = str_subtract(dir, "/")
    return dir

# change to base directory
def setDir():
    if (getDir() != "vertexCover" and getDir() != "experiments"):
        if (getDir() == "trunk"):
            os.chdir("..")
            os.chdir("..")
        elif (getDir() == "testoutput"):
            os.chdir("..")
            os.chdir("..")
            os.chdir("..")
        else:
            os.chdir("..")
    return

# get patho of right directories
def results():
    setDir()
    return os.getcwd() + "/results"

def vertexCover():
    setDir()
    return os.getcwd() + "/vertexCover"

def graph():
    setDir()
    return os.getcwd() + "/graphs"

def graphExplorer():
    setDir()
    return os.getcwd() + "/graphExplorer"

def hyperbolic():
    setDir()
    return os.getcwd() + "/graphlib/trunk"

def hyperbolicGraphs():
    setDir()
    return os.getcwd() + "/graphlib/trunk/testoutput"
