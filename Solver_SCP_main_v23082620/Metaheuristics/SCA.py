#SCA
import random
import math
import numpy as np


def iterarSCA(maxIter, t, dimension, poblacion, bestSolution):
    # a is a constant number, paper recommend use 2
    a = 2
    # aplicacion de la ecuacion 3.4
    r1 = a - (t * (a / maxIter))
    for i in range(poblacion.__len__()):
        for j in range(dimension):
            rand1 = random.uniform(0.0, 1.0)
            r2 =  (2 * math.pi) * rand1
            rand2 = random.uniform(0.0, 1.0)
            r3 = 2 * rand2
            r4 = random.uniform(0.0, 1.0)
            if r4 < 0.5:
                poblacion[i][j] = poblacion[i][j] + ( ( ( r1 * math.sin(r2)) * abs( ( r3 * bestSolution[j] ) - poblacion[i][j] ) ) )
            else:
                poblacion[i][j] = poblacion[i][j] + ( ( ( r1 * math.cos(r2)) * abs( ( r3 * bestSolution[j] ) - poblacion[i][j] ) ) )
    return np.array(poblacion)