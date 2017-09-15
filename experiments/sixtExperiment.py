import graphGenerator
import os

import random
import subprocess
import math
import dir
import numpy




# (1) We first set up a text file in the
# right folder, to save the results

st = dir.results() + "/sixtExperiment.txt"
file = open(st, 'w')
file.write("Algorithm "
           + "nodes "
           + "edges "
           + "power_exponent "
           + "steps "
           + "covering_size "
           + "edges_covered "
           + "fitness\n")

for numberNodes in range (100, 1000, 50) :

    # (2) We first generate a random graph that has a
    # given number of nodes and with exp = 2.5
    
    sn = "cd " + dir.hyperbolic()
    process = subprocess.Popen(sn, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    #process = subprocess.Popen(sn, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    hypCmd = sn + "; " + "scons;" "./build_debug/singleexperiment --seed=1" \
                + " --save_graph=testoutput/graph --rgmodel=hyperbolic --sort --n=" \
                + str(numberNodes) \
                + " --gamma=2.5 --giant"
    #print(hypCmd)
    process = subprocess.Popen(hypCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(process.stdout.read()).split(" ")

    # posptocess and rename graph with adj list
    fl = dir.hyperbolicGraphs() + '/graph-links.txt'
    with open(fl, 'r') as myfile:
        data = myfile.read().replace('\t', ' ')
    myfile.close()

    # get number of nodes
    data2 = data.replace('\n', ' ')
    data3 = data2.split(" ")
    numberNodes1 = len(numpy.unique(data3)) - 1

    # save to new file 

    rl = dir.graph() + "/hyperbolicGraph_" + str(numberNodes1) + "nodes_2.5exp.txt"
    newfile = open(rl, 'w')
    newfile.write(data)
    newfile.close()
    remove2 = "rm " + dir.hyperbolicGraphs() + "/graph-links.txt"
    process = subprocess.Popen(remove2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(process.stdout.read()).split(" ")

    # transfer and rename text file with embedding
    move1 = "mv " + dir.hyperbolicGraphs() + "/graph-embedded.txt " \
    + dir.graph() + "/hyperbolicGraph-embedded_" \
        + str(numberNodes1) + "nodes_2.5exp.txt"
    process = subprocess.Popen(move1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(process.stdout.read()).split(" ")
    remove1 = "rm " + dir.hyperbolicGraphs() + "/graph-embedded.txt"
    process = subprocess.Popen(remove1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(process.stdout.read()).split(" ")

    # (3) We then run the algorithm via a C++
    # executable and save the results 100 times

    # control status
    print("Status: graph of " + str(numberNodes1) + " nodes being processed.")

    for i in range (1, 100) :

        # directory of new graph
        x = dir.graph() + "/hyperbolicGraph_" + str(numberNodes1) + "nodes_2.5exp.txt"

        # make command
        st = dir.graphExplorer()
        seed = i
        cmd = st + "/graphExplorerExe EA " \
                 + x + " 1 " \
                 + str(int(8 * numberNodes1 * math.log(numberNodes1))) + " " \
                 + str(random.randint(1, 100))

        # make subprocess
        process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        # wait for the process to terminate
        out = str(process.stdout.read()).split(" ")

        # print to file
        file.write("EA " + str(numberNodes1) + " "
                         + out[1]
                         + " 2.5 "
                         + str(int(8 * numberNodes1 * math.log(numberNodes1)))
                         + " " + out[2]
                         + " " + out[3]
                         + " " + dir.str_subtract(out[4], "'"))
        file.write("\n")



file.close()
