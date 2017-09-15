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

* source = C++ source code for the experiments
* results = .txt files with results and RStudio postprocesses

The results are organized as follows.

* calibration = parameter calibration experiments
* variance = posterior noise variance experiments
* runtime = running time analysis
* reevaluation = running tine with reevaluation analysis

Each experiments is saved in a separate .txt file. Postprocesses in .R and .pdf files have same name as experiments.

## Conclusions
We compare empirically the run time behavior of four different bio-inspired search heuristics. Our testbed is the fitness function oneMax, which is a simple unimodal function with posterior noise. All algorithms have local parameters, which influence their run time. We study the dependence of the parameter on the amount of noise and empirically determine for each algorithm the optimal parameter setting depending on the noise. We give statistical predictions for each parameter's asymptotic behavior. 

We are then able to compare the algorithms with optimal parameter settings depending on the level of noise. We observe a strict hierarchy in how well the algorithms can deal with noise. From worst to best this is (m + 1)-EA, (m + 1)-GA, l-MMASib, and cGA.

A common technique to deal with noisy fitness functions is resampling. We therefore also study the optimal number of samples for a given noise level. With optimal resampling we observe improved run times for the (m + 1)-EA and (m + 1)-GA, which scaled least graceful with noise. However, with optimal resampling both of them have exponential run time. We prove that resampling is redundant for any algorithm with quadratic run time, thus showing that cGA and l-MMASib do not benefit from this operator. Therefore, all four algorithms reach run time complexity quadratic in the posterior noise standard deviation. 

Overall, this study shows that resampling is more beneficial than crossover, for algorithms that perform poorly in noisy environments. By far the best scaling behaviour was achieved with EDAs, suggesting that such algorithms can handle noise implicitly. We plan to validate all hereby presented statistical models analytically in the future.

## Acknowledgements

The research leading to these results has received funding from the European Union Seventh Framework Programme (FP7/2007-2013) under grant agreement no.618091 (SAGE) and from the German Science Foundation (DFG) under grant agreement FR 2988 (TOSU).
