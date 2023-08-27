El presente proyecto está dividido en diferentes carpetas las cuales son las siguientes:

1. BD: 
    Esta carpeta incluye la base de datos sqlite del proyecto donde se almacena los experimentos.
2. Discretization: 
    Esta carpeta tiene todos los apartados de discretización de las metaheurísticas continuas. Estan diferentes funciones de transferencias y reglas de binarización para utilizar
3. Diversity:
    En esta carpeta se encuentra una métrica de análisis de diversidad de la población en el proceso metaheurístico
4. Metaheuristics:
    En esta carpeta se encuentran las diferentes metaheurísticas implementadas. Hasta el momento se encuentran las siguientes mh implementadas:
        1. Genetic Algorithm
        2. Grey Wolf Optimizer
        3. Moth-Flame Optimization
        4. Pendulum Search Algorithm
        5. Sine Cosine Algorithm
        6. Whale Optimization Algorithm
    EN ESTA CARPETA DEBEN IMPLEMENTAR SU metaheurísticas
5. Problem:
    En esta carpeta se encuentran todos los componentes de los problemas de optimización implementados. En este proyecto solo se encuentran dos problemas:
        1. Funciones matemáticas Benchmark: Estas son las funciones matemáticas Benchmark clásicas resueltas en la literatura. Son problemas continuos
        2. Set Covering Problem. Este es un problema de optimización combinatorial de minimización clásico. 
           En el archivo "problem.py" se encuentra la lectura de instancias, cálculo de fitness, test de factibilidad de soluciones y reparación de soluciones.
6. Resultados: 
    En esta carpeta se almacena los archivos temporales de resultados que luego son almacenados en la base datos. 
    Además, acá se mostrarán los archivos de análisis realizados a los experimentos ejecutados luego de ejecutar el archivo "analisisSCP.py" o "analisisBEN.py"
7. Solver:
    En esta carpeta se encuentran los solver de cada problema de optimización. Cuando se agrega una metaheurística nueva, en los archivos de esta carpeta se deben incorporar.
8. util:
    En esta carpeta se encuentran apartados genéricos que son utilizados por diferentes programnas del proyecto.

Para ejecutar los experimentos, primero deben poblar la base de datos. Para esto, deben ejecutar el archivo "poblarDB.py"

Una vez poblada la base de datos, deben ejecutar el archivo "main.py" en cual comenzará a llamar los experimentos que se encuentran pendientes en la base de datos.

DEPENDENCIAS:

La versión de python es 3.10.5 de 64 bit 
numpy==1.23.1
scipy==1.8.1
matplotlib==3.5.2
pandas==1.4.3
seaborn==0.11.2
