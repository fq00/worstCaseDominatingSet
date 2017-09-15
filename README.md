# worstCaseDominatingSet
## Abstract
It has been experimentally observed that real-world networks follow certain topological properties, such as small-world, power-law etc. To study these networks, many random graph models, such as Preferential Attachment, have been proposed.
We consider the deterministic properties which capture power-law degree distribution and degeneracy. Networks with these properties are known as scale-free networks in the literature. Many interesting problems remain NP-hard on scale-free networks. We study the relationship between scale-free properties and the approximation-ratio of some commonly used evolutionary algorithms.
For the Vertex Cover, we observe experimentally that the (1+1) EA always gives the better result than a greedy local search, even when it runs for only 2(n log n) steps. We give the construction of a scale-free network in which the (1+1) EA takes more time than a greedy algorithm to obtain the optimal solution.

## Algorithms

The (1 + 1)-EA is a search heuristics inspired by the process of natural selection. Typically, it requires as input a population of strings of fixed length n. After an offspring is generated, a mutation factor is introduced, to ensure full objective space exploration. The fitness is then computed, and the less desirable result is discarded.

The greedy algorithm is deterministic, and it is specifically designed to find a minimum vertex cover of an input graph. It iteratively adds nodes, which have highest degree to the cover, until all edges are covered.


## Files and folders
The project is organized as follows.

* experiments = Python files to manage the C++ executable
* graphExplorer = The C++ source kernel
* graph = all input graphs for the experiments
* results = all experimental results, including R postprocess files

## Conclusions
We looked at the approximation ratio and run time analysis of single-objective EAs, for well known NP-hard problems on the graphs with deterministic PLB properties, and the power-law exponent β > 2. We analyze the (1+1) EA for the maximum dominating set, maximum vertex cover and connected dominating set problems. We show that the (1+1) EA obtain constant-factor approximation ratio within polynomial run time.
We observe experimentally that the (1+1) EA always produces better results than the greedy algorithm for the minimum vertex cover problem. We showthat the (1+1) EA gives better approximation ratio than greedy on the Chung-Lu and Hyperbolic model. We observe that on the Hyperbolic model the (1+1) EA reaches better approximation ratio than in the Chung-Lu case. We give a worst case instance with the PLB properties, where greedy algorithm obtain an optimal solution, but the (1+1) EA gives worst possible solution with constant probability. We conclude that the EAs for the above-mentioned problems on the graphs with PLB properties and β > 2, obtain better approximation than the known worst-case approximation. This implies that topological properties of real-world instances play an important role in the performance of EAs.
