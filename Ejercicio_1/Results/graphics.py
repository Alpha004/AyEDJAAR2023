import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

C_LANGUAGE = 'C++'
PYTHON_LANGUAGE = 'Python'
GOLANG_LANGUAGE = 'Golang'

SUFIX_CSV = 'Sort.csv'

def fixFloat(numero):
    return round(float(numero.replace("\n", "")),6)

if __name__ == '__main__':
    args = sys.argv[1:]
    python_data = []
    golang_data = []
    c_data = []
    python_max_lim = 0.0
    python_min_lim = 0.0
    golang_max_lim = 0.0
    golang_min_lim = 0.0
    c_max_lim = 0.0
    c_min_lim = 0.0
    xdata = list(range(5))
    if len(args) == 2:
        algorithm = str(args[0])
        size_data = str(args[1])
        with open('./'+PYTHON_LANGUAGE+'/'+algorithm+'SortResults_'+size_data+'.txt') as f:
            python_data = f.readlines()
        f.close()
        with open('./'+GOLANG_LANGUAGE+'/'+algorithm+'SortResults_'+size_data+'.txt') as f:
            golang_data = f.readlines()
        f.close()
        with open('./'+C_LANGUAGE+'/'+algorithm+'SortResults_'+size_data+'.txt') as f:
            c_data = f.readlines()
        f.close()          
        with open('./'+ PYTHON_LANGUAGE +'_'+algorithm+SUFIX_CSV) as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=","))
            for row in csv_reader:
                if str(row[0]).strip() == size_data:
                    python_max_lim = float(row[3])
                    python_min_lim = float(row[4])                    
                    break
        csv_file.close()
        with open('./'+ GOLANG_LANGUAGE +'_'+algorithm+SUFIX_CSV) as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=","))
            for row in csv_reader:
                if str(row[0]).strip() == size_data:
                    golang_max_lim = float(row[3])
                    golang_min_lim = float(row[4])
                    break
        csv_file.close()
        with open('./'+ C_LANGUAGE +'_'+algorithm+SUFIX_CSV) as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=","))
            for row in csv_reader:
                if str(row[0]).strip() == size_data:
                    c_max_lim = float(row[3])
                    c_min_lim = float(row[4])
                    break
        csv_file.close()
        max_limit = round(float(max([python_max_lim,golang_max_lim,c_max_lim])),6)
        min_limit = round(float(min([python_min_lim,golang_min_lim,c_min_lim])),6)
        #PLOT
        python_data = list(map(fixFloat,python_data))
        golang_data = list(map(fixFloat,golang_data))
        c_data = list(map(fixFloat,c_data))
        print(python_data)
        print(golang_data)
        print(c_data)
        print(max_limit)
        print(min_limit)
        plt.plot(xdata, python_data, label="Python")
        plt.plot(xdata, golang_data, label="Go")
        plt.plot(xdata, c_data, label="C++")
        plt.xlim([0, 5])  
        plt.ylim([min_limit, max_limit])
        plt.title("COMPARACION - " + algorithm.upper() + " - " + size_data + " ITEMS")
        plt.legend(loc="upper left")
        plt.xlabel("Nro de Ejecuciones")
        plt.ylabel("Tiempo de Procesamiento")
        plt.savefig('./Graficas/'+algorithm+'_'+size_data+'.png')
        plt.show()
    else:
        print("Provee el algoritmo y el tamaño a realizar la grafica")
