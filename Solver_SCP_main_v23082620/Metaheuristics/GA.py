import random
import numpy as np
from util.util import selectionSort

# selection of parent
def select_parent(population, fitness):
    position = selectionSort(fitness)
    # parent1 = random.choice(population)
    # parent2 = random.choice(population)
    
    parent1 = population[position[0]]
    parent2 = population[position[1]]
    
    # print(len(population))
    # while parent2 == parent1:
    #     parent2 = random.choice(population)
    
    return parent1, parent2

# crossover operator
def crossover(parent1, parent2, prob_crossover):
    # pivot = random.randint(1, len(parent1) -1 )
    pivot = int(np.round( (len(parent1) * prob_crossover) , 0))
    
    child1 = parent1[:pivot] + parent2[pivot:]
    child2 = parent2[:pivot] + parent1[pivot:]
    
    return child1, child2

# mutation operator
def mutate(chromsome, mutation_rate):
    mutated_chromsome = []
    for gen in chromsome:
        if random.uniform(0, 1) < mutation_rate:
            mutated_chromsome.append( 1 - gen )
        else:
            mutated_chromsome.append(gen)
        
    return mutated_chromsome

def iterarGA(population, fitness, cross, muta):
    new_population = []
    
    for i in range( len(population) // 2):
        parent1, parent2 = select_parent(population, fitness)
        child1, child2 = crossover(parent1, parent2, cross)
        child1 = mutate(child1, muta)
        child2 = mutate(child1, muta)
        new_population.extend([child1, child2])    
    
    return np.array(new_population)