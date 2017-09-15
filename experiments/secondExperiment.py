import graphGenerator
import random
import subprocess
import math
import dir

st = dir.results() + "/secondExperiment.txt"
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

    # control status
    print("Status: graph of " + str(numberNodes) + " nodes being processed.")


    # make command
    st = dir.graph() + "/powerLawGraph_" + str(numberNodes) + "nodes_2.5deg.txt"
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






