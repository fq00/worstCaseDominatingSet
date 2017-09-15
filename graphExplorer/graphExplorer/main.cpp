//
//  main.cpp
//  graphExplorer
//
//  Created by Francesco Quinzan on 29/11/2016.
//  Copyright © 2016 Francesco Quinzan. All rights reserved.
//

#include <iostream>
#include <vector>
#include "inputManager.hpp"
#include "EA.hpp"
#include "greedy.hpp"


using namespace std;

int main(int argc, const char * argv[]) {
    
    if(argc == 6){
        
        /* import graph */
        std::string file = argv[2];
        class graph graph(file);
        
        /*  choose algorithm */
        std::string algr = argv[1];
        
        if(algr == "EA"){
        
            /* initialize and run EA */
            class EA EA(&graph,  atol(argv[3]), atol(argv[4]));
            std::vector<unsigned long> solution;
            if (EA.run(&solution, atol(argv[5])) != -1){
                
                std::cout << " " << solution.at(0);
                std::cout << " " << solution.at(1);
                std::cout << " " << solution.at(2);
                std::cout << " " << solution.at(3);
                
                
            }
            else
                std::cout << "process aborted" << std::endl;
        }
    }
    
    else if(argc == 3){
        
        /* import graph */
        std::string file = argv[2];
        class graph graph(file);
        
        /*  choose algorithm */
        std::string algr = argv[1];
        
        if(algr == "greedy"){
            
            /* initialize and run EA */
            class greedy greedy(&graph);
            std::vector<unsigned long> solution(greedy.run());

            
            std::cout << " " << solution.at(0);
            std::cout << " " << solution.at(1);
            std::cout << " " << solution.at(2);
            std::cout << " " << solution.at(3);
            
        }
    }
    
    else {
    
        std::cout << "wrong command" << std::endl;
        
    }
    
    return 0;
}
