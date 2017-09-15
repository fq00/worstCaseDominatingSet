import graphGenerator
import os

import random
import subprocess
import math
import dir




# (1) We first set up a text file in the
# right folder, to save the results

st = dir.results() + "/eightExperiment.txt"
print(st)
file = open(st, 'w')
file.write("Algorithm "
           + "nodes "
           + "edges "
           + "power_exponent "
           + "steps "
           + "covering_size "
           + "edges_covered "
           + "time\n")

nNodes = (100, 149, 196, 246, 296, 341, 386, 444, 489, 542, 590, 626, 673, 718, 761, 810, 855, 903)

for numberNodes1 in nNodes :
    
    # (2) We then run the algorithm via a C++
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
