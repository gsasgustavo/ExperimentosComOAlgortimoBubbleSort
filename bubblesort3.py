import os
import datetime
import re
import psutil


def bubblesort3(dataset):
    start_time = datetime.datetime.now()
    pid = os.getpid()
    py = psutil.Process(pid)
    exchanges = 0
    comparisons = 0

    with open(dataset+'.csv', encoding="utf8") as myfile:
        data = myfile.read()
        data = re.split('\n|,', data)

    j, k = 1, True
    while j <= len(data) and k:
        k = False
        for i in range(len(data)-1):
            comparisons += 1
            if data[i] < data[i+1]:
                exchanges += 1
                k, aux = True, data[i]
                data[i], data[i+1] = data[i+1], aux
        j += 1

    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000

    file = open('bubblesort3-'+dataset+'.txt', 'w')
    file.write('Quantidade de comparações'+': '+str(comparisons)+'\n')
    file.write('Quantidade de trocas'+': '+str(exchanges)+'\n')
    file.write('Tempo de execução'+': '+str(execution_time)+'\n')
    file.write('Consumo de CPU'+': '+str(py.cpu_times()[0])+'\n')
    file.write('Consumo de memória'+': '+str(py.memory_info()[0]/8000000000)+'\n')
    file.close()


bubblesort3('dataset-2-a')
bubblesort3('dataset-2-b')
bubblesort3('dataset-2-c')
