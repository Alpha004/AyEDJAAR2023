import numpy as np
import sys
import os
import csv
import operator

if __name__ == '__main__':
    args = sys.argv[1:]
    data = []
    csvData = []
    if len(args) == 3:
        secondHeader = str(args[1])
        algorithm = str(args[2])
        files = [f for f in os.listdir(str(args[0])) if algorithm in f]
        print(files)
        for file in files:
            sizeCurrentFile = int(file.split('_')[1].split('.')[0])
            with open(args[0] + '\\' + file) as f:
                data = f.readlines()            
            f.close()
            for i in range(len(data)):
                data[i] = float(data[i].replace("\n", ""))                        
            prom = sum(data) / len(data)
            st_dev = np.std(data)
            csvData.append({'cantidad': sizeCurrentFile, secondHeader: round(prom, 6), 'desv_estandar': round(st_dev, 6), 'lim_max': round(prom+st_dev, 6), 'lim_min': round(prom-st_dev, 6)})
            
            #print("El promedio es: " + str(prom) +" y la desviacion estandar es: " + str(st_dev)) ##str(round(float(st_dev),5))
        csvData = sorted(csvData, key=operator.itemgetter('cantidad'))
        print(csvData)
        columns = ['cantidad', secondHeader,'desv_estandar','lim_max','lim_min']
        with open(secondHeader + '_' + algorithm +'.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=columns )
            writer.writeheader()
            for csvrow in csvData:
                writer.writerow(csvrow)
        file.close()
    else:
        print("brinde la ruta a calcular el promedio y desviacion estandar")
        exit(0)