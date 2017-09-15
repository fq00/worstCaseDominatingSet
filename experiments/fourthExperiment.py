import graphGenerator
import random
import subprocess
import math
import dir

st = dir.results() + "/fourthExperiment.txt"
file = open(st, 'w')
file.write("Algorithm "
           + "nodes "
           + "edges "
           + "power_exponent "
           + "steps "
           + "covering_size "
           + "edges_covered "
           + "fitness\n")

numberNodes = 500
exp = 2.1

while (exp < 3.0) :

    # control status
    print("Status: graph of " + str(numberNodes) + " nodes being processed.")


    # make command
    st = dir.graph() + "/powerLawGraph_" + str(numberNodes) + "nodes_" + str(exp) + "deg.txt"
    cmd = dir.graphExplorer() + "/graphExplorerExe greedy " + st

    # make subprocess
    process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    # wait for the process to terminate
    out = str(process.stdout.read()).split(" ")

    # print to file
    file.write("greedy " + str(numberNodes) + " "
                         + out[1] + " "
                         + str(exp) + " "
                         + str(int(8 * numberNodes * math.log(numberNodes)))
                         + " " + out[2]
                         + " " + out[3]
                         + " " + dir.str_subtract(out[4], "'"))
    file.write("\n")

    #increase exponent
    exp = round(exp + 0.05, 2)


file.close()
