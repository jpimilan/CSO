import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns
from util import util
from BD.sqlite import BD

# Directorio donde se almacenarán los resultados
dirResultado = './Resultados/'

# Abrir archivos para almacenar resúmenes de fitness, tiempos y porcentajes
archivoResumenFitness = open(f'{dirResultado}resumen_fitness_SCP.csv', 'w')
archivoResumenTimes = open(f'{dirResultado}resumen_times_SCP.csv', 'w')
archivoResumenPercentage = open(f'{dirResultado}resumen_percentage_SCP.csv', 'w')

# Escribir encabezados en los archivos
archivoResumenFitness.write("instance,best,avg. fitness, std fitness,best,avg. fitness, std fitness,best,avg. fitness, std fitness, best,avg. fitness, std fitness\n")
archivoResumenTimes.write("instance, min time (s), avg. time (s), std time (s), min time (s), avg. time (s), std time (s), min time (s), avg. time (s), std time (s), min time (s), avg. time (s), std time (s)\n")
archivoResumenPercentage.write("instance, avg. XPL%, avg. XPT%, avg. XPL%, avg. XPT%, avg. XPL%, avg. XPT%, avg. XPL%, avg. XPT%\n")

# Variable para habilitar o deshabilitar la generación de gráficos
graficos = False

# Conexión a la base de datos
bd = BD()

# Obtener instancias de problemas 'scp41'
instancias = bd.obtenerInstancias('scp46')

# Iterar sobre las instancias de problemas
for instancia in instancias:
    print(instancia)

    # Obtener información de los archivos relacionados con la instancia
    blob = bd.obtenerArchivos(instancia[1])
    corrida = 1

    # Crear archivo para almacenar datos de fitness
    archivoFitness = open(f'{dirResultado}fitness_'+instancia[1].split(".")[0]+'.csv', 'w')
    archivoFitness.write('MH,FITNESS\n')

# Listas para almacenar datos de diferentes metaheurísticas
    fitnessSCA = [] 
    fitnessGWO = [] 
    fitnessWOA = [] 
    fitnessPSA = []
    #SE AGREGA LA NUEVA MH
    fitnessCSO = []

    timeSCA = []
    timeGWO = []
    timeWOA = []
    timePSA = []
    #SE AGREGA LA NUEVA MH
    timeCSO = []

    xplSCA = [] 
    xplGWO = [] 
    xplWOA = [] 
    xplPSA = []
    #SE AGREGA LA NUEVA MH
    xplCSO = []

    xptSCA = []
    xptGWO = []
    xptWOA = []
    xptPSA = []
    #SE AGREGA LA NUEVA MH
    xptCSO = []
    
    bestFitnessSCA = []
    bestFitnessGWO = []
    bestFitnessWOA = []
    bestFitnessPSA = []
    #SE AGREGA LA NUEVA MH
    bestFitnessCSO = []

    bestTimeSCA = []
    bestTimeGWO = []
    bestTimeWOA = []
    bestTimePSA = []
    #SE AGREGA LA NUEVA MH
    bestTimeCSO = []

    # Iterar sobre los archivos obtenidos
    for d in blob:
        
        nombreArchivo = d[0]
        archivo = d[1]
# Crear archivo intermedio para procesar datos
        direccionDestiono = './Resultados/Transitorio/'+nombreArchivo+'.csv'
        # print("-------------------------------------------------------------------------------")
        util.writeTofile(archivo,direccionDestiono)

        # Leer datos del archivo intermedio
        data = pd.read_csv(direccionDestiono)

        # Extraer información del nombre del archivo
        mh = nombreArchivo.split('_')[0]
        problem = nombreArchivo.split('_')[1]

        iteraciones = data['iter']
        fitness     = data['fitness']
        time        = data['time']
        xpl         = data['XPL']
        xpt         = data['XPT']

        # Almacenar datos según la metaheurística
        if mh == 'PSA':
            fitnessPSA.append(np.min(fitness))
            timePSA.append(np.round(np.sum(time),3))
            xplPSA.append(np.round(np.mean(xpl), decimals=2))
            xptPSA.append(np.round(np.mean(xpt), decimals=2))
            archivoFitness.write(f'PSA,{str(np.min(fitness))}\n')
        if mh == 'SCA':
            fitnessSCA.append(np.min(fitness))
            timeSCA.append(np.round(np.sum(time),3))
            xplSCA.append(np.round(np.mean(xpl), decimals=2))
            xptSCA.append(np.round(np.mean(xpt), decimals=2))
            archivoFitness.write(f'SCA,{str(np.min(fitness))}\n')
        if mh == 'GWO':
            fitnessGWO.append(np.min(fitness))
            timeGWO.append(np.round(np.sum(time),3))
            xplGWO.append(np.round(np.mean(xpl), decimals=2))
            xptGWO.append(np.round(np.mean(xpt), decimals=2))
            archivoFitness.write(f'GWO,{str(np.min(fitness))}\n')
        if mh == 'WOA':
            fitnessWOA.append(np.min(fitness))
            timeWOA.append(np.round(np.sum(time),3))
            xplWOA.append(np.round(np.mean(xpl), decimals=2))
            xptWOA.append(np.round(np.mean(xpt), decimals=2))
            archivoFitness.write(f'WOA,{str(np.min(fitness))}\n')
        if mh == 'CSO':
            fitnessCSO.append(np.min(fitness))
            timeCSO.append(np.round(np.sum(time),3))
            xplCSO.append(np.round(np.mean(xpl), decimals=2))
            xptCSO.append(np.round(np.mean(xpt), decimals=2))
            archivoFitness.write(f'CSO,{str(np.min(fitness))}\n')
            
        # Generar gráficos si está habilitado
        if graficos:

            # fig , ax = plt.subplots()
            # ax.plot(iteraciones,fitness)
            # ax.set_title(f'Convergence {mh} \n {problem} run {corrida}')
            # ax.set_ylabel("Fitness")
            # ax.set_xlabel("Iteration")
            # plt.savefig(f'{dirResultado}/Graficos/Coverange_{mh}_{problem}_{corrida}.pdf')
            # plt.close('all')
            # print(f'Grafico de covergencia realizado {mh} {problem} ')
            
            figPER, axPER = plt.subplots()
            axPER.plot(iteraciones, xpl, color="r", label=r"$\overline{XPL}$"+": "+str(np.round(np.mean(xpl), decimals=2))+"%")
            axPER.plot(iteraciones, xpt, color="b", label=r"$\overline{XPT}$"+": "+str(np.round(np.mean(xpt), decimals=2))+"%")
            axPER.set_title(f'XPL% - XPT% {mh} \n {problem} run {corrida}')
            axPER.set_ylabel("Percentage")
            axPER.set_xlabel("Iteration")
            axPER.legend(loc = 'upper right')
            plt.savefig(f'{dirResultado}/Graficos/Percentage_{mh}_{problem}_{corrida}.pdf')
            plt.close('all')
            print(f'Grafico de exploracion y explotacion realizado para {mh}, problema: {problem}, corrida: {corrida} ')
        
        corrida +=1
        
        if corrida == 32:
            corrida = 1
        
        os.remove('./Resultados/Transitorio/'+nombreArchivo+'.csv')
        
    # archivoResumenFitness.write(f'''{problem},{np.min(fitnessGWO)},{np.round(np.average(fitnessGWO),3)},{np.round(np.std(fitnessGWO),3)},{np.min(fitnessPSA)},{np.round(np.average(fitnessPSA),3)},{np.round(np.std(fitnessPSA),3)},{np.min(fitnessSCA)},{np.round(np.average(fitnessSCA),3)},{np.round(np.std(fitnessSCA),3)},{np.min(fitnessWOA)},{np.round(np.average(fitnessWOA),3)},{np.round(np.std(fitnessWOA),3)} \n''')
    # archivoResumenTimes.write(f'''{problem},{np.min(timeGWO)},{np.round(np.average(timeGWO),3)},{np.round(np.std(timeGWO),3)},{np.min(timePSA)},{np.round(np.average(timePSA),3)},{np.round(np.std(timePSA),3)},{np.min(timeSCA)},{np.round(np.average(timeSCA),3)},{np.round(np.std(timeSCA),3)},{np.min(timeWOA)},{np.round(np.average(timeWOA),3)},{np.round(np.std(timeWOA),3)} \n''')
    # archivoResumenPercentage.write(f'''{problem},{np.round(np.average(xplGWO),3)},{np.round(np.average(xptGWO),3)},{np.round(np.average(xplPSA),3)},{np.round(np.average(xptPSA),3)},{np.round(np.average(xplSCA),3)},{np.round(np.average(xptSCA),3)},{np.round(np.average(xplWOA),3)},{np.round(np.average(xptWOA),3)} \n''')

    archivoResumenFitness.write(f'''{problem},{np.min(fitnessCSO)},{np.round(np.average(fitnessCSO),3)},{np.round(np.std(fitnessCSO),3)} \n''')
    archivoResumenTimes.write(f'''{problem},{np.min(timeCSO)},{np.round(np.average(timeCSO),3)},{np.round(np.std(timeCSO),3)} \n''')
    archivoResumenPercentage.write(f'''{problem},{np.round(np.average(xplCSO),3)},{np.round(np.average(xptCSO),3)} \n''')

    blob = bd.obtenerMejoresArchivos(instancia[1])
    
    for d in blob:

        nombreArchivo = d[3]
        archivo = d[5]

        direccionDestiono = './Resultados/Transitorio/'+nombreArchivo+'.csv'
        util.writeTofile(archivo,direccionDestiono)
        
        data = pd.read_csv(direccionDestiono)
        
        mh = d[1]#nombreArchivo.split('_')[0]
        problem = d[4].split('_')[1]

        iteraciones = data['iter']
        fitness     = data['fitness']
        time        = data['time']
        xpl         = data['XPL']
        xpt         = data['XPT']
        
        if mh == 'PSA':
            bestFitnessPSA      = fitness
            bestTimePSA         = time
        if mh == 'SCA':
            bestFitnessSCA      = fitness
            bestTimeSCA         = time
        if mh == 'GWO':
            bestFitnessGWO      = fitness
            bestTimeGWO         = time
        if mh == 'WOA':
            bestFitnessWOA      = fitness
            bestTimeWOA         = time
        if mh == 'CSO':
            bestFitnessCSO      = fitness
            bestTimeCSO         = time
        
        os.remove('./Resultados/Transitorio/'+nombreArchivo+'.csv')

    print("------------------------------------------------------------------------------------------------------------")
    figPER, axPER = plt.subplots()
    # axPER.plot(iteraciones, bestFitnessGWO, color="r", label="GWO")
    # axPER.plot(iteraciones, bestFitnessSCA, color="b", label="SCA")
    # axPER.plot(iteraciones, bestFitnessPSA, color="g", label="PSA")
    # axPER.plot(iteraciones, bestFitnessWOA, color="y", label="WOA")
    axPER.plot(iteraciones, bestFitnessCSO, color="y", label="CSO")
    axPER.set_title(f'Coverage \n {problem}')
    axPER.set_ylabel("Fitness")
    axPER.set_xlabel("Iteration")
    axPER.legend(loc = 'upper right')
    plt.savefig(f'{dirResultado}/Best/fitness_{problem}.pdf')
    plt.close('all')
    print(f'Grafico de fitness realizado {problem} ')
    
    figPER, axPER = plt.subplots()
    # axPER.plot(iteraciones, bestFitnessGWO, color="r", label="GWO")
    # axPER.plot(iteraciones, bestFitnessSCA, color="b", label="SCA")
    # axPER.plot(iteraciones, bestFitnessPSA, color="g", label="PSA")
    # axPER.plot(iteraciones, bestFitnessWOA, color="y", label="WOA")
    axPER.plot(iteraciones, bestFitnessCSO, color="y", label="CSO")
    axPER.set_title(f'Time (s) \n {problem}')
    axPER.set_ylabel("Time (s)")
    axPER.set_xlabel("Iteration")
    axPER.legend(loc = 'lower right')
    plt.savefig(f'{dirResultado}/Best/time_{problem}.pdf')
    plt.close('all')
    print(f'Grafico de time realizado {problem} ')
    
    
    archivoFitness.close()
    
    print("------------------------------------------------------------------------------------------------------------")
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    datos = pd.read_csv(dirResultado+"/fitness_"+instancia[1].split(".")[0]+'.csv')
    figFitness, axFitness = plt.subplots()
    axFitness = sns.boxplot(x='MH', y='FITNESS', data=datos)
    axFitness.set_title(f'Fitness \n{instancia[1].split(".")[0]}', loc="center", fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'black'})
    axFitness.set_ylabel("Fitness")
    axFitness.set_xlabel("Metaheuristics")
    figFitness.savefig(dirResultado+"/boxplot/boxplot_fitness_"+instancia[1].split(".")[0]+'.pdf')
    plt.close('all')
    print(f'Grafico de boxplot con fitness para la instancia {instancia[1].split(".")[0]} realizado con exito')
    
    figFitness, axFitness = plt.subplots()
    axFitness = sns.violinplot(x='MH', y='FITNESS', data=datos, gridsize=50)
    axFitness.set_title(f'Fitness \n{instancia[1].split(".")[0]}', loc="center", fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'black'})
    axFitness.set_ylabel("Fitness")
    axFitness.set_xlabel("Metaheuristics")
    figFitness.savefig(dirResultado+"/violinplot/violinplot_fitness_"+instancia[1].split(".")[0]+'.pdf')
    plt.close('all')
    print(f'Grafico de violines con fitness para la instancia {instancia[1].split(".")[0]} realizado con exito')
    
    os.remove(dirResultado+"/fitness_"+instancia[1].split(".")[0]+'.csv')
    
    print("------------------------------------------------------------------------------------------------------------")

archivoResumenFitness.close()
archivoResumenTimes.close()
archivoResumenPercentage.close()
        