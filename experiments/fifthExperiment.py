from multiprocessing import Pool
import random
import subprocess
import math
import os

# string subtract
def dir_str_subtract(s1, s2):
    for ch in s2:
        if ch in s1:
            s1 = s1.replace(ch, '', 1)
    return s1

# get name of the current directory
def dir_getDir():

    s1 = os.getcwd()
    s2 = os.path.dirname(s1)

    dir = dir_str_subtract(s1, s2)
    dir = dir_str_subtract(dir, "/")

    return dir

# change to base directory
def dir_setDir():
    if (dir_getDir() != "vertexCover"):
        os.chdir("..")
    return

# get patho of right directories
def dir_results():
    dir_setDir()
    return os.getcwd() + "/results"

def dir_vertexCover():
    dir_setDir()
    return os.getcwd() + "/vertexCover"

def dir_graph():
    dir_setDir()
    return os.getcwd() + "/graphs"

def dir_graphExplorer():
    dir_setDir()
    return os.getcwd() + "/graphExplorer"


# function to run experiment

def experiment(population) :

    numberNodes = 5242

    # graph diectory
    graph = dir_graph() + "/ca-GrQc_clean.txt"

    # make command
    cmd = dir_graphExplorer() + "/graphExplorerExe EA " \
        + graph + " " \
        + str(population) + " " \
        + str(int(numberNodes * math.log(numberNodes) - population)) + " " \
        + str(random.randint(1, 100))

    # make subprocess
    process = subprocess.Popen(cmd, shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    # wait for the process to terminate
    out = str(process.stdout.read()).split(" ")

    # return results
    st = dir_results() + "/fifthExperiment.txt"
    file = open(st, 'a')
    file.write("ca-GrQc_clean " + "EA "
              + str(population)
              + " " + str(numberNodes)
              + " " + out[1]
              + " " + str(int(numberNodes * math.log(numberNodes) - population + 1))
              + " " + str(int(numberNodes * math.log(numberNodes)))
              + " " + out[2]
              + " " + out[3]
              + " " + dir_str_subtract(out[4], "'")
              + "\n")
    file.close()

# main
# set up header and initial parameters

st = dir_results() + "/fifthExperiment.txt"
file = open(st, 'w')
file.write( "Graph "
           + "Algorithm "
           + "population "
           + "nodes "
           + "edges "
           + "steps "
           + "fitness_evaluations "
           + "covering_size "
           + "edges_covered "
           + "fitness\n")
file.close()

# run experiments in parallel

input = list(range(10, 110, 10))
for j in range(1, 99):
    for i in range(10, 110, 10):
        input.append(i)

pool = Pool()
results = pool.map(experiment, input)

file.close()
