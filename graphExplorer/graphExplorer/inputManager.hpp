//
//  inputManager.hpp
//  graphExplorer
//
//  Created by Francesco Quinzan on 29/11/2016.
//  Copyright © 2016 Francesco Quinzan. All rights reserved.
//

#ifndef inputManager_hpp
#define inputManager_hpp

#include <stdio.h>
#include <fstream>
#include <vector>
#include <functional>
#include <iostream>
#include <unordered_set>

using namespace std;

class graph{
    
    /* preprecess input data */
    void addEdge(char [256]);
    void import(std::string);
    void setVariables();
    void clean();
    
public:
    
    /* constructor: import file */
    graph (std::string fileName){
        graph::import(fileName);
        graph::setVariables();
        return;
    };
    
    /* public function: make the degree table */
    void groupDegree();
    
    /* graph variables: number of edges and nodes */
    unsigned long numberNodes;
    unsigned long numberEdges;
    
    /* graph is rapresented as adjacent matrix */
    std::vector<std::vector<unsigned long> > adjList;
    
    /* graph is rapresented as node degree */
    std::vector<unsigned long> degree;
    
};

#endif /* inputManager_hpp */
