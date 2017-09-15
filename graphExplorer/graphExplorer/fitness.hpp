//
//  fitness.hpp
//  graphExplorer
//
//  Created by Francesco Quinzan on 29/11/2016.
//  Copyright © 2016 Francesco Quinzan. All rights reserved.
//

#ifndef fitness_hpp
#define fitness_hpp

#include <stdio.h>
#include <vector>
#include <algorithm>
//#include <unordered_set>
#include <thread>
#include <pthread.h>

#include "unorderedIndex.hpp"
#include "inputManager.hpp"

using namespace std;

class fitness {

    /* pointer to a graph to compute the fitness */
    class graph *graph;
    
public:
    
    /* count the number of true occurrences in imput array */
    inline unsigned long oneMax(std::vector<bool> *x){
        return std::count(x->begin(), x->end(), true);
    }

    /* count the number of uncovered edges */
    unsigned long u(std::vector<bool> *);
    
    /* constructor */
    fitness(class graph * graph){
        fitness::graph = graph;
    }
    
    /* return the fitness of boolean array */
    inline unsigned long f(std::vector<bool> *x){
        return std::pow(fitness::graph->numberNodes, 2) * fitness::u(x) + fitness::oneMax(x);
    }

};

#endif /* fitness_hpp */

