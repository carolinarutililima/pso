#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:48:28 2021

@author: carolinarutilidelima
"""

import math
import numpy as np 
import matplotlib.pyplot as plt
from ypstruct import structure # encapsulates variables 
import pso 




# def function to optimize ackley fun
def function(x):
    D = 10
    cosx = 0
    listcos = []
    listquad = []
    for i in x:
        cosx = math.cos(2*math.pi*i) 
        listcos.append(cosx)
        listquad.append(i**2)
    sumcos = sum(listcos) 
    sumx = sum(listquad)    
    p1 = -0.2* math.sqrt(1/D * sumx)
    p2 = 1/D *  sumcos  
    fun = 20 + math.exp(1) - 20*math.exp(p1) - math.exp(p2)
    return fun



# Variables according to problem definition
problem = structure()
problem.costfunc = function
problem.varmin = - 32 # -100
problem.varmax = 32 # 100



# PSO parameters
params = structure()
params.maxit = 1000000 # max iterations number
params.accep = 0.01 # acceptance for stop the alg
params.nv = 10 # number of members in a particle
params.particle_size = 50 # number of particles
params.w = 0.9  # inertia constant
params.c1 = 2.05 # cognitive constant 
params.c2 = 2 # social constant



#Run PSO
 
output = pso.run(problem, params)



# Results  
plt.plot(output.bestcost, 'b', linewidth = 3 )
plt.semilogy(output.bestcost)
plt.xlim(0,output.it)
plt.xlabel('Iterations')
plt.ylabel('Output')
plt.title('PSO Algorithm')
plt.show()
    
    