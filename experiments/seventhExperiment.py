import graphGenerator
import random
import subprocess
import math
import dir

st = dir.results() + "/seventhExperiment.txt"
file = open(st, 'w')
file.write("Algorithm "
           + "nodes "
           + "edges "
           + "power_exponent "
           + "steps "
           + "covering_size "
           + "edges_covered "
           + "fitness\n")

nNodes = (100, 149, 196, 246, 296, 341, 386, 444, 489, 542, 590, 626, 673, 718, 761, 810, 855, 903)

for numberNodes in nNodes :

    # control status
    print("Status: graph of " + str(numberNodes) + " nodes being processed.")


    # make command
    st = dir.graph() + "/hyperbolicGraph_" + str(numberNodes) + "nodes_2.5exp.txt"
    print(st)
    cmd = dir.graphExplorer() + "/graphExplorerExe greedy " + st

    # make subprocess
    process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    # wait for the process to terminate
    out = str(process.stdout.read()).split(" ")

    # print to file
    file.write("greedy " + str(numberNodes) + " "
                         + out[1]
                         + " 2.5 "
                         + str(int(8 * numberNodes * math.log(numberNodes)))
                         + " " + out[2]
                         + " " + out[3]
                         + " " + dir.str_subtract(out[4], "'"))
    file.write("\n")


file.close()