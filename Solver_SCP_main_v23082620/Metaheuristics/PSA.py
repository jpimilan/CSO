#PSA
import random
import numpy as np
def iterarPSA(maxIter, t, dimension, poblacion, bestSolution):
    for i in range(poblacion.__len__()):
        for j in range(dimension):
            rand = random.random()
            pend = 2 * np.exp( -t / maxIter ) * ( np.cos( 2 * np.pi * rand ) )
            poblacion[i][j] = poblacion[i][j] + ( pend * ( bestSolution[j] - poblacion[i][j] ) )
    return np.array(poblacion)