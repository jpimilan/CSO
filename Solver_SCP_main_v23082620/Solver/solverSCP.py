import numpy as np
import os
from Problem.SCP.problem import SCP
from Metaheuristics.GWO import iterarGWO
from Metaheuristics.PSA import iterarPSA
from Metaheuristics.SCA import iterarSCA
from Metaheuristics.WOA import iterarWOA
from Metaheuristics.MFO import iterarMFO
from Metaheuristics.GA import iterarGA

#----------------------------------------------
from Metaheuristics.CSO import iterarCSO
#----------------------------------------------

from Diversity.hussainDiversity import diversidadHussain
from Diversity.XPLXTP import porcentajesXLPXPT
import time
from Discretization import discretization as b
from util import util
from BD.sqlite import BD

def solverSCP(id, mh, maxIter, pop, instancia, DS, repairType, param):
    
    dirResult = './Resultados/'
    instance = SCP(instancia)
    
    # tomo el tiempo inicial de la ejecucion
    initialTime = time.time()
    
    tiempoInicializacion1 = time.time()

    print("------------------------------------------------------------------------------------------------------")
    print("instancia SCP a resolver: "+instancia)
    
    results = open(dirResult+mh+"_"+instancia.split(".")[0]+"_"+str(id)+".csv", "w")
    results.write(
        f'iter,fitness,time,XPL,XPT,DIV\n'
    )
    
    # Genero una población inicial binaria, esto ya que nuestro problema es binario
    poblacion = np.random.randint(low=0, high=2, size = (pop, instance.getColumns()))

    maxDiversidad = diversidadHussain(poblacion)
    XPL , XPT, state = porcentajesXLPXPT(maxDiversidad, maxDiversidad)
    
    # Genero un vector donde almacenaré los fitness de cada individuo
    fitness = np.zeros(pop)

    # Genero un vetor dedonde tendré mis soluciones rankeadas
    solutionsRanking = np.zeros(pop)
    
    # calculo de factibilidad de cada individuo y calculo del fitness inicial
    for i in range(poblacion.__len__()):
        flag, aux = instance.factibilityTest(poblacion[i])
        if not flag: #solucion infactible
            poblacion[i] = instance.repair(poblacion[i], repairType)
            

        fitness[i] = instance.fitness(poblacion[i])
        
    solutionsRanking = np.argsort(fitness) # rankings de los mejores fitnes
    bestRowAux = solutionsRanking[0]
    # DETERMINO MI MEJOR SOLUCION Y LA GUARDO 
    Best = poblacion[bestRowAux].copy()
    BestFitness = fitness[bestRowAux]
    
    # PARA MFO
    BestFitnessArray = fitness[solutionsRanking] 
    bestSolutions = poblacion[solutionsRanking]
    
    matrixBin = poblacion.copy()
    
    tiempoInicializacion2 = time.time()
    
    # mostramos nuestro fitness iniciales
    print("------------------------------------------------------------------------------------------------------")
    print("fitness incial: "+str(fitness))
    print("Best fitness inicial: "+str(BestFitness))
    print("------------------------------------------------------------------------------------------------------")
    if mh == "GA":
        print("COMIENZA A TRABAJAR LA METAHEURISTICA "+mh+ " / Reparacion: "+repairType)
    else: 
        print("COMIENZA A TRABAJAR LA METAHEURISTICA "+mh+ " / Binarizacion: "+ str(DS) + " / Reparacion: "+repairType)
    print("------------------------------------------------------------------------------------------------------")
    print("iteracion: "+
            str(0)+
            ", best: "+str(BestFitness)+
            ", mejor iter: "+str(fitness[solutionsRanking[0]])+
            ", peor iter: "+str(fitness[solutionsRanking[pop-1]])+
            ", optimo: "+str(instance.getOptimum())+
            ", time (s): "+str(round(tiempoInicializacion2-tiempoInicializacion1,3))+
            ", XPT: "+str(XPT)+
            ", XPL: "+str(XPL)+
            ", DIV: "+str(maxDiversidad))
    results.write(
        f'0,{str(BestFitness)},{str(round(tiempoInicializacion2-tiempoInicializacion1,3))},{str(XPL)},{str(XPT)},{maxDiversidad}\n'
    )
    
    for iter in range(0, maxIter):
        # obtengo mi tiempo inicial
        timerStart = time.time()
        
        if mh == "MFO":
            for i in range(bestSolutions.__len__()):
                BestFitnessArray[i] = instance.fitness(bestSolutions[i])
        
        # perturbo la poblacion con la metaheuristica, pueden usar SCA y GWO
        # en las funciones internas tenemos los otros dos for, for de individuos y for de dimensiones
        # print(poblacion)
        #----------------------------------------------
        if mh=="CSO":
            poblacion = iterarCSO(instance.getColumns(),poblacion.tolist(), Best.tolist())
        #----------------------------------------------
        if mh == "SCA":
            poblacion = iterarSCA(maxIter, iter, instance.getColumns(), poblacion.tolist(), Best.tolist())
        if mh == "GWO":
            poblacion = iterarGWO(maxIter, iter, instance.getColumns(), poblacion.tolist(), fitness.tolist(), 'MIN')
        if mh == 'WOA':
            poblacion = iterarWOA(maxIter, iter, instance.getColumns(), poblacion.tolist(), Best.tolist())
        if mh == 'PSA':
            poblacion = iterarPSA(maxIter, iter, instance.getColumns(), poblacion.tolist(), Best.tolist())
        if mh == "MFO":
            poblacion, bestSolutions = iterarMFO(maxIter, iter, instance.getColumns(), len(poblacion), poblacion, bestSolutions, fitness, BestFitnessArray )
        if mh == "GA":
            
            cross = float(param.split(";")[0].split(":")[1])
            muta = float(param.split(";")[1].split(":")[1])
            poblacion = iterarGA(poblacion.tolist(), fitness, cross, muta)
        
        # Binarizo, calculo de factibilidad de cada individuo y calculo del fitness
        for i in range(poblacion.__len__()):

            if mh != "GA":
                poblacion[i] = b.aplicarBinarizacion(poblacion[i].tolist(), DS[0], DS[1], Best, matrixBin[i].tolist())

            flag, aux = instance.factibilityTest(poblacion[i])
            # print(aux)
            if not flag: #solucion infactible
                poblacion[i] = instance.repair(poblacion[i], repairType)
                

            fitness[i] = instance.fitness(poblacion[i])


        solutionsRanking = np.argsort(fitness) # rankings de los mejores fitness
        
        #Conservo el Best
        if fitness[solutionsRanking[0]] < BestFitness:
            BestFitness = fitness[solutionsRanking[0]]
            Best = poblacion[solutionsRanking[0]]
        matrixBin = poblacion.copy()

        div_t = diversidadHussain(poblacion)

        if maxDiversidad < div_t:
            maxDiversidad = div_t
            
        XPL , XPT, state = porcentajesXLPXPT(div_t, maxDiversidad)

        timerFinal = time.time()
        # calculo mi tiempo para la iteracion t
        timeEjecuted = timerFinal - timerStart
        
        print("iteracion: "+
            str(iter+1)+
            ", best: "+str(BestFitness)+
            ", mejor iter: "+str(fitness[solutionsRanking[0]])+
            ", peor iter: "+str(fitness[solutionsRanking[pop-1]])+
            ", optimo: "+str(instance.getOptimum())+
            ", time (s): "+str(round(timeEjecuted,3))+
            ", XPT: "+str(XPT)+
            ", XPL: "+str(XPL)+
            ", DIV: "+str(div_t))
        
        results.write(
            f'{iter+1},{str(BestFitness)},{str(round(timeEjecuted,3))},{str(XPL)},{str(XPT)},{str(div_t)}\n'
        )
    print("------------------------------------------------------------------------------------------------------")
    print("Best fitness: "+str(BestFitness))
    print("Cantidad de columnas seleccionadas: "+str(sum(Best)))
    print("------------------------------------------------------------------------------------------------------")
    finalTime = time.time()
    tiempoEjecucion = finalTime - initialTime
    print("Tiempo de ejecucion (s): "+str(tiempoEjecucion))
    results.close()
    
    binary = util.convert_into_binary(dirResult+mh+"_"+instancia.split(".")[0]+"_"+str(id)+".csv")

    nombre_archivo = mh+"_"+instancia.split(".")[0]

    bd = BD()
    bd.insertarIteraciones(nombre_archivo, binary, id)
    bd.insertarResultados(BestFitness, tiempoEjecucion, Best, id)
    bd.actualizarExperimento(id, 'terminado')
    
    os.remove(dirResult+mh+"_"+instancia.split(".")[0]+"_"+str(id)+".csv")
    
    
    