//
//  unorderedIndex.hpp
//  graphExplorer
//
//  Created by Francesco Quinzan on 21/12/2016.
//  Copyright © 2016 Francesco Quinzan. All rights reserved.
//

#ifndef unorderedIndex_hpp
#define unorderedIndex_hpp

#include <stdio.h>
#include <iostream>
#include <unordered_set>

/* we overload the unordered set template class
 to easily initate a set of indexes */

class unordered_index : public std::unordered_set<unsigned long>{
    
public:
    
    void init (unsigned long a, unsigned long b){
        
        try{
            unordered_set::clear();
            for (unsigned long i = a; i < b; i++)
                unordered_set::insert(i);
            return;
        }
        catch(std::bad_alloc&)
        {
            std::cout << "Out of memory while making unordered index" << std::endl;
            exit (EXIT_FAILURE);
        }
        catch(...){
            std::cout << "Exception while making unordered index" << std::endl;
            exit (EXIT_FAILURE);
        }
        
    }
    
    void init (unsigned long b){
        
        try{
            unordered_set::clear();
            for (unsigned long i = 0; i < b; i++)
                unordered_set::insert(i);
            return;
        }
        catch(std::bad_alloc&)
        {
            std::cout << "Out of memory while making unordered index" << std::endl;
            exit (EXIT_FAILURE);
        }
        catch(...){
            std::cout << "Exception while making unordered index" << std::endl;
            exit (EXIT_FAILURE);
        }
    }
    
};

#endif /* unorderedIndex_hpp */
