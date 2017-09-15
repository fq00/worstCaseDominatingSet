import graphGenerator
import random
import subprocess
import math
import dir





# (1) We first set up a text file in the
# right folder, to save the results

st = dir.results() + "/firstExperiment.txt"
file = open(st, 'w')
file.write("Algorithm "
           + "nodes "
           + "edges "
           + "power_exponent "
           + "steps "
           + "covering_size "
           + "edges_covered "
           + "fitness\n")

for numberNodes in range (100, 150, 50) :

    # (2) We first generate a random graph that has a
    # given number of nodes and with exp = 2.5

    x = graphGenerator.makeGraph(numberNodes, exp = 2.5)

    # (3) We then run the algorithm via a C++
    # executable and save the results 100 times

    # control status
    print("Status: graph of " + str(numberNodes) + " nodes being processed.")

    for i in range (1, 100) :

        # make command
        st = dir.graphExplorer()
        seed = i
        cmd = st + "/graphExplorerExe EA " \
                  + x + " " \
                  + str(int(8 * numberNodes * math.log(numberNodes))) + " " \
                  + str(random.randint(1, 100))

        # make subprocess
        process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        # wait for the process to terminate
        out = str(process.stdout.read()).split(" ")

        # print to file
        file.write("EA " + str(numberNodes) + " "
                         + out[1]
                         + " 2.5 "
                         + str(int(8 * numberNodes * math.log(numberNodes)))
                         + " " + out[2]
                         + " " + out[3]
                         + " " + dir.str_subtract(out[4], "'"))
        file.write("\n")


file.close()






