//
//  EA.cpp
//  graphExplorer
//
//  Created by Francesco Quinzan on 29/11/2016.
//  Copyright © 2016 Francesco Quinzan. All rights reserved.
//

#include "EA.hpp"

/* run algorithm */
int EA::run(std::vector<unsigned long> *solution, unsigned long seed){
    
    try{
        
        auto flag = 0;
        
        /* set fitness and initial generator */
        EA::generator.seed(seed);
        class fitness fitness(EA::graph);
        std::vector<unsigned long> fvals;
    
        if (EA::makePopulation(&fvals, &fitness) != -1){
    
            unsigned long t = 1;
            while (t < EA::maxStep){
        
                /* perform mutation */
                if(EA::uniformMutation(population::getRandom(), population::getMutant()) != 0){
                    flag = -1;
                    break;
                }
                fvals.back() = fitness.f(population::getMutant());
        
                /* discard worst element */
                if(EA::cleanPopulation(&fvals) != 0){
                    flag = -1;
                    break;
                };
        
                /* step increase */
                t++;
                
            }
    
            /* return fitness and vertex cover size */
            if(flag != -1){
                auto mindx = std::min_element(fvals.begin(), fvals.end() - 1) - fvals.begin();
                std::cout << mindx << std::endl;
                solution->push_back(EA::graph->numberEdges);
                solution->push_back(fitness.oneMax(population::get(mindx)));
                solution->push_back(EA::graph->numberEdges - fitness.u(population::get(mindx)));
                solution->push_back(fitness.f(population::get(mindx)));
            }
    
            return flag;
        
        }
        else
            return -1;
    }
    catch(...){
        std::cout << "Exception while running algorithm" << std::endl;
    }
    return -1;
    
};

/* generate an array uniformly at random */
int EA::uniformMutation(std::vector<bool> *x){
    
    try{
        /* prepare for mutation */
        std::vector<bool>().swap(*x);
        long double mutationRate = std::pow(2.0, -1.0);
        
        /* create uniform array */
        for(unsigned long i = 0; i < EA::graph->numberNodes; i++){
            if (EA::uniformReal(1.0) <= mutationRate)
                x->push_back(true);
            else
                x->push_back(false);
        }
        return 0;
    }
    catch(std::bad_alloc&)
    {
        std::cout << "Out of memory while generating new array" << std::endl;
    }
    catch(...)
    {
        std::cout << "Exception while generating new array" << std::endl;
    }
    return -1;
    
};

/* uniform muation */
int EA::uniformMutation(std::vector<bool> *x, std::vector<bool> *y){
    
    try{
        /* prepare for mutation */
        std::vector<bool>().swap(*y);
        long double uniformProb = std::pow((long double) x->size(), -1.0);
    
        /* perform mutation on y */
        for(std::vector<bool>::iterator it = x->begin(); it != x->end(); ++it){
            if (EA::uniformReal(1.0) <= uniformProb)
                y->push_back(!(*it));
            else
                y->push_back(*it);
        }
        return 0;
    }
    catch (...)
    {
            std::cout << "Exception while introduciong mutation" << std::endl;
    }
    return -1;
    
};

/* make population */
int EA::makePopulation(std::vector<unsigned long> *fvals, class fitness *fitness){
    
    try{
        if(population::allocate() != -1){
            
            /* create initial population */
            for (unsigned long i = 0; i < population::populationSize; i++){
                EA::uniformMutation(population::get(i));
                fvals->push_back(fitness->f(population::get(i)));
            }
        
            /* allocate space for mutant */
            fvals->push_back(0);
            return 0;
            }
        else
            return -1;
    }
    catch(std::bad_alloc&)
    {
        std::cout << "Out of memory while generating population" << std::endl;
    }
    catch(...)
    {
        std::cout << "Exception while generating population" << std::endl;    
    }
    return -1;
    
};

/* clean population */
int EA::cleanPopulation(std::vector<unsigned long> *fvals){

    try{
        auto maxIndex = std::max_element(fvals->begin(), fvals->end()) - fvals->begin();
        if(maxIndex != population::populationSize){
            population::get(maxIndex)->swap(*population::getMutant());
            fvals->at(maxIndex) = fvals->back();
        }
        return 0;
    }
    catch(...)
    {
        std::cout << "Exception while cleaning population" << std::endl;
    }
    return -1;
    
};
