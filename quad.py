#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:49:56 2021

@author: carolinarutilidelima
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
from ypstruct import structure
import pso 



# def function to optimize quadract fun
def function(x):
    summ = 0
    lst_summ = []
    for i in x:
        summ = summ + i
        quad = summ ** 2
        lst_summ.append(quad)
    
    y = sum(lst_summ)
    
    return y


# Variables according to problem definition
problem = structure()
problem.costfunc = function
problem.varmin = - 100 # -100
problem.varmax = 100 # 100



# PSO parameters
params = structure()
params.maxit = 100000 # max iterations number
params.accep = 100 # acceptance for stop the alg
params.nv = 10 # number of members in a particle
params.particle_size = 50 # number of particles
params.w = 0.9  # inertia constant
params.c1 = 2.05 # cognitive constant 
params.c2 = 2 # social constant



#Run PSO
 
output = pso.run(problem, params)



# Results  
plt.plot(output.bestcost, 'g', linewidth = 3 )
plt.semilogy(output.bestcost)
plt.xlim(0,output.it)
plt.xlabel('Iterations')
plt.ylabel('Output')
plt.title('PSO Algorithm')
plt.show()
    