//
//  EA.hpp
//  graphExplorer
//
//  Created by Francesco Quinzan on 29/11/2016.
//  Copyright © 2016 Francesco Quinzan. All rights reserved.
//

#ifndef EA_hpp
#define EA_hpp

#include <stdio.h>
#include <random>
#include <math.h>
#include "inputManager.hpp"
#include "fitness.hpp"

using namespace std;

class population{

protected:
    
    /* variables */
    std::vector<std::vector<bool> > population;
    std::vector<bool> mutant;
    
    /* allocate population in memory */
    int allocate(){
        try{
            population::population.resize(population::populationSize);
            for(std::vector<std::vector<bool> >::iterator it = population::population.begin(); it != population::population.end(); ++it){
                (*it).resize(population::problemSize);
            }
            population::mutant.resize(population::problemSize);
            return 0;
        }
        catch(std::bad_alloc&){
            std::cout << "Out of memory while saving population" << std::endl;
        }
        catch(...){
            std::cout << "Exception while saving population" << std::endl;
        }
        return -1;
    }


    
public:
    
    /* variables */
    unsigned long populationSize, problemSize;
    
    /* get element at random */
    inline std::vector<bool> * getRandom(){
        auto index = rand() % population::populationSize;
        return &population.at(index);
    }
    
    /* get element by index */
    inline std::vector<bool> * get(unsigned long index){
        return &population.at(index);
    }
    
    /* get pointer to mutant */
    inline std::vector<bool> * getMutant(){
        return &mutant;
    }
};

class EA : public population{
    
    /* graph to solve */
    struct graph *graph;
    
    /* algorithm parameters */
    unsigned long maxStep;
    
    /* random number generator and distribution */
    std::mt19937 generator;
    inline long double uniformReal(long double x){
        std::uniform_real_distribution<long double> uniformRealDistribution(0.0, x);
        return(uniformRealDistribution(EA::generator));
    };
    
    /* algorithmic operations */
    int uniformMutation(std::vector<bool> *);
    int uniformMutation(std::vector<bool> *, std::vector<bool> *);
    
    /* population operation */
    int makePopulation(std::vector<unsigned long> *, class fitness *);
    int cleanPopulation(std::vector<unsigned long> *);
    
    
public:
    
    /* constructor */
    inline EA(class graph *graph, unsigned long populationSize, unsigned long maxStep){
        
        /* derived class */
        EA::graph = graph;
        EA::maxStep = maxStep;
        
        /* base class */
        population::populationSize = populationSize;
        population::problemSize = EA::graph->numberNodes;
        
    };
    
    /* run algorithm given random seed */
    int run(std::vector<unsigned long> *, unsigned long);
    
};


#endif /* EA_hpp */
