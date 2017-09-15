//
//  fitness.cpp
//  graphExplorer
//
//  Created by Francesco Quinzan on 29/11/2016.
//  Copyright © 2016 Francesco Quinzan. All rights reserved.
//

#include "fitness.hpp"

/* count the number of uncovered edges */
unsigned long fitness::u(std::vector<bool> *x){

    try{
        
        /* allocate set of inices */
        class unordered_index index1, index2;
        index1.init(fitness::graph->adjList.size());
        index2.init(fitness::graph->adjList.size());
    
        /* find all edges that are covered */
        for(unsigned long i = 0; i < x->size(); i++){
            if(x->at(i) == true){
                for(auto &j : index1){
                    if(fitness::graph->adjList.at(j).front() == i or fitness::graph->adjList.at(j).back() == i)
                        index2.erase(j);
                }
                index1 = index2;
            }
        }
        return index1.size();
    
    }
    catch(...){
        std::cout << "Exception while computing fitness" << std::endl;
        exit (EXIT_FAILURE);
    }
    
}
