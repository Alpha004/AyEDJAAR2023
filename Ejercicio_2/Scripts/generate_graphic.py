import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

PATH = '../Results/'
ACO_RESULTS = 'ACO_Results.txt'
BF_RESULTS = 'BF_Results.txt'

def fixFloat(numero):
    return round(float(numero.replace("\n", "")),6)

if __name__ == '__main__':
    args = sys.argv[1:]
    aco_data = []
    bf_data = []
    
    aco_max_lim = 0.0
    aco_min_lim = 0.0
    bf_max_lim = 0.0
    bf_min_lim = 0.0    
    xdata = list(range(4,15))
    
    with open(PATH + ACO_RESULTS) as f:
        aco_data = f.readlines()
    f.close()
    with open(PATH + BF_RESULTS) as f:
        bf_data = f.readlines()
    f.close()                
    #PLOT
    aco_data = list(map(fixFloat,aco_data))
    bf_data = list(map(fixFloat,bf_data))
    print(aco_data)
    print(bf_data)
    print(xdata)
    plt.plot(xdata, aco_data, label="ACO")
    plt.plot(xdata, bf_data, label="Brute Force")    
    plt.xlim([2, 15])  
    plt.ylim([0, 1000])
    plt.title("COMPARACION - HEURISTICA VS BRUTE FORCE")
    plt.legend(loc="upper left")
    plt.xlabel("Tamaño")
    plt.ylabel("Tiempo de Procesamiento")
    plt.savefig('../Results/heuristica_results.png')
    plt.show()

