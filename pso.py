#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:03:16 2021

@author: carolinarutilidelima
"""
import random
from ypstruct import structure


def run(problem, params):

    #Problem definition 
    costfunc = problem.costfunc
    varmin = problem.varmin
    varmax = problem.varmax
    
    
    
    
    # Parameters 
    maxit = params.maxit # max iterations number
    accep = params.accep # acceptance for stop the alg
    nv = params.nv  # members inside the particle
    particle_size = params.particle_size  # number of particles
    w = params.w  # inertia constant
    c1 = params.c1 # cognitive constant 
    c2 = params.c2# social constant
    
    class Particle:
        
        def __init__(self,bounds):
            self.particle_position = []  # particle position
            self.particle_velocity = []  # particle velocity
            self.local_best_particle_position = [] # best position of the particle 
            self.fitness_local_best_particle_postiion = initial_fitness # initial objective function value of the best particle position
            self.fitness_particle_position = initial_fitness # objective function value of the particle position
            
            for i in range(nv):
                
                self.particle_position.append(random.randint(bounds[0], bounds[1]))
                #self.particle_velocity.append(random.uniform(-1,1)) # generate random inital velocity
                self.particle_velocity.append(random.randint(bounds[0], bounds[1])) # generate random inital velocity
                            
                
                
        def evaluate(self, objective_function):
            self.fitness_particle_position = objective_function(self.particle_position)
            if self.fitness_particle_position < self.fitness_local_best_particle_postiion:
                self.local_best_particle_position = self.particle_position # update the local best
                self.fitness_local_best_particle_postiion = self.fitness_particle_position # update the fitness of the loca best               
            

        
        def update_velocity(self, global_best_particle_position, bounds):
            for i in range(nv):
                r1 = random.random()
                r2 = random.random()
                
                
                
                cognitive_velocity = c1 * r1 * (self.local_best_particle_position[i] - self.particle_position[i])
                social_velocity = c2 * r2 * (global_best_particle_position[i] - self.particle_position[i])
                self.particle_velocity[i] = w * self.particle_velocity[i] + cognitive_velocity + social_velocity
                
                
                if self.particle_velocity[i] > bounds[1]:
                    self.particle_velocity[i] = bounds[1]
                # check and repair to satisfy the lower bounds
                if self.particle_velocity[i] < bounds[0]:
                    self.particle_velocity[i] = bounds[0]
                
        def update_position(self, bounds):
            for i in range(nv):
                self.particle_position[i] = self.particle_position[i] + self.particle_velocity[i]
                
                # check and repair to satisfy the upper bounds
                if self.particle_position[i] > bounds[1]:
                    #print("aqui posi")
                    self.particle_position[i] = bounds[1]
                # check and repair to satisfy the lower bounds
                if self.particle_position[i] < bounds[0]:
                   # print("aqui")
                    self.particle_position[i] = bounds[0]
                    
    
    
    initial_fitness = float("inf") # for minimization problem  
    
    
    fitness_global_best_particle_position = initial_fitness
    global_best_particle_position = []
    swarm_particle = []
    bounds = [varmin, varmax]
    
    for i in range(particle_size):
        swarm_particle.append(Particle(bounds))
        
    
    A = []
    
    it = 0 
    
    while fitness_global_best_particle_position > accep and maxit > it:
        
        
        for i in range(particle_size):
            swarm_particle[i].evaluate(costfunc)
            
            

            
            if swarm_particle[i].fitness_particle_position < fitness_global_best_particle_position:
                global_best_particle_position =  list(swarm_particle[i].particle_position)
                fitness_global_best_particle_position = float(swarm_particle[i].fitness_particle_position)
                        
                
        for i in range(particle_size):
            swarm_particle[i].update_velocity(global_best_particle_position, bounds)
            swarm_particle[i].update_position(bounds)
                    
                
            
        A.append(fitness_global_best_particle_position) # record the best fitness
        
        print( "Interation {}: best output/cost = {}".format(it ,fitness_global_best_particle_position))
        
        
        it = it + 1
        
        
    
    output = structure()
    output.bestcost = A
    output.it = it
    
    return output 

