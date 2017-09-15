try:

    # from matplotlib import network as nx

    import numpy as np
    import math
    import networkx as nx

except:

    raise

import math
import dir

# this function creates a power-law
# degree graph of a given number of
# endges and saves it in memory

def powerLawGraph(nodes, exp, dir) :

    # create power-law graph

    list6 = []
    for i in range(0, nodes):
        a = 407 / ((i + 1) ** (1 / (exp - 1)))
        list6.append(math.ceil(a))
    GE = nx.expected_degree_graph(list6, selfloops=False)

    # save power-law graph

    #nx.write_edgelist(GE, dir)
    fh = open(dir, 'wb')
    nx.write_edgelist(GE, fh, data=False)
    #nx.write_gexf(GE, dir)

    return

# this function creates a file with
# a random graph and saves it in a
# proper file

def makeGraph(nodes, exp) :

    # make the proper name
    name = "powerLawGraph_" + str(nodes) + "nodes_" + str(exp) + "deg"
    st = dir.graph() + "/" + str(name) + ".txt"

    # create the graph
    powerLawGraph(nodes, exp, st)

    return st
