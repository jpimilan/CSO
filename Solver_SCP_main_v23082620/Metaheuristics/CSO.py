import random
import numpy as np
from util.util import selectionSort


# Función de iteración CSO
def iterarCSO(dimension, poblacion, MejorSolucion):
    Kp = 1.0
    Ki = 0.1
    Kd = 0.01
    prev_error = 0
    prev_integral = 0
    prev_derivative = 0
    
    # Iterar sobre cada solución en la población
    for i in range(len(poblacion)):
        # Inicializar la suma de fuerzas para esta solución
        suma_fuerzas = np.zeros(dimension)
        
        # Calcular la contribución de cada gato (solución) a las fuerzas
        for j in range(dimension):
            error = MejorSolucion[j] - poblacion[i][j]
            derivative = error - prev_error
            integral = prev_integral + error
            
            # Calcular la fuerza CSO para esta dimensión
            fuerza = Kp * error + Ki * integral + Kd * derivative
            
            # Acumular la fuerza en la suma total de fuerzas
            suma_fuerzas[j] = fuerza
            
            # Actualizar los valores previos para la próxima iteración
            prev_error = error
            prev_integral = integral
            prev_derivative = derivative
        
        # Actualizar la posición del gato (solución) utilizando las fuerzas acumuladas
        poblacion[i] = poblacion[i] + suma_fuerzas
    
    return np.array(poblacion)