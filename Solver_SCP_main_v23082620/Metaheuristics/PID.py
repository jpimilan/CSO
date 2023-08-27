import random
import numpy as np
from util.util import selectionSort

# iteracion PID
def iterarPID(dimension, poblacion, MejorSolucion):
    Kp = 1.0
    Ki = 0.1
    Kd = 0.01
    prev_error = 0
    prev_integral = 0
    prev_derivative = 0
    
    for i in range(poblacion.__len__()):
        for j in range(dimension):
            error = MejorSolucion[i] - poblacion[i][j]
            derivative = error - prev_error
            integral = prev_integral + error
            
            poblacion[i][j] += Kp * error + Ki * integral + Kd * derivative
            
            prev_error = error
            prev_integral = integral
            prev_derivative = derivative

    return np.array(poblacion)