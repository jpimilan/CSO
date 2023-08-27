#WOA
import math
import random
import numpy as np
def iterarWOA(maxIter, t, dimension, poblacion, bestSolution):
    a = 2 - ((2*t)/maxIter)
    b = 1
    for i in range(poblacion.__len__()):
        for j in range(dimension):
            #  p is a random number into [0,1]
            p = random.uniform(0.0 , 1.0)
            # aplicacion de ecuacion 2.3
            r = random.uniform(0.0 , 1.0)
            A = 2 * a * (r - a) 
            # aplicacion de ecuacion 2.4
            r = random.uniform(0.0 , 1.0)
            C =  2 * r
            # l is a random number into [-1,1]
            l = random.uniform(-1.0 , 1.0)
            # aplicacion de ecuacion 2.6
            if p < 0.5:
                if abs(A) < 1: 
                    # aplicacion ecuacion de movimiento 2.1
                    D = abs( ( C * bestSolution[j] ) - poblacion[i][j] )
                    # aplicacion ecuacion de movimiento 2.2
                    poblacion[i][j] = bestSolution[j] - ( A * D )
                else:
                    posAleatorea = random.randint( 0, poblacion.__len__() - 1 ) # seleccionar un individuo al azar
                    # aplicacion de ecuacion 2.7
                    D = abs( ( C * poblacion[posAleatorea][j] ) - poblacion[i][j] )
                    # aplicacion de ecuacion 2.8
                    poblacion[i][j] = poblacion[posAleatorea][j] - ( A * D )
            else:
                # aplicacion de ecuacion de movimiento 2.5
                DPrima = bestSolution[j] - poblacion[i][j]
                poblacion[i][j] = ( DPrima * math.exp( b * l) * math.cos(2 * math.pi * l) ) + bestSolution[j]
    return np.array(poblacion)