//
//  greedy.hpp
//  graphExplorer
//
//  Created by Francesco Quinzan on 01/12/2016.
//  Copyright © 2016 Francesco Quinzan. All rights reserved.
//

#ifndef greedy_hpp
#define greedy_hpp

#include <stdio.h>
#include <vector>
#include <algorithm>

#include "unorderedIndex.hpp"
#include "fitness.hpp"
#include "inputManager.hpp"

class greedy{
    
    /* graph to solve */
    struct graph *graph;
    
    /* algorithmic operations */
    void uniformArray(std::vector<bool> *);
    void groupDegree(struct graph *, std::vector<long> *);
    
public:
    
    /* constructor */
    inline greedy(class graph *graph){
        greedy::graph = graph;
    };
    
    /* run algorithm */
    std::vector<unsigned long> run();

};

#endif /* greedy_hpp */
