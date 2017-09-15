//
//  greedy.cpp
//  graphExplorer
//
//  Created by Francesco Quinzan on 01/12/2016.
//  Copyright © 2016 Francesco Quinzan. All rights reserved.
//

#include "greedy.hpp"

std::vector<unsigned long>  greedy::run(){
    
    try{
        /* initial settings */
        unsigned long m = 0;
        class fitness fitness(greedy::graph);
    
        /* (1) initiate right set of indeces */
        class unordered_index index;
        index.init(greedy::graph->numberNodes);
    
        /* (2) compute the degree for all nodes */
        greedy::graph->groupDegree();
    
        /* (3) make first solution */
        std::vector<bool> x;
        x.resize(greedy::graph->numberNodes, false);
    
        /* (4) add nodes at each iteration */
        while (fitness.u(&x) != 0){
        
            /* find maximal element */
            m = *index.begin();
            for (const auto& i: index){
                if(greedy::graph->degree.at(i) >= greedy::graph->degree.at(m))
                    m = i;
            }
        
            /* add node to the covering and time step */
            x.at(m) = true;
            index.erase(m);
        }
    
        /* return fitness and vertex cover size */
        std::vector<unsigned long> solution;
    
        solution.push_back(greedy::graph->numberEdges);
        solution.push_back(fitness.oneMax(&x));
        solution.push_back(greedy::graph->numberEdges - fitness.u(&x));
        solution.push_back(fitness.f(&x));
    
        return(solution);
    }
    catch(...){
        std::cout << "Exception while running greedy" << std::endl;
        exit(EXIT_FAILURE);
    }
}
