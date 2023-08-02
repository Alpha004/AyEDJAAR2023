import numpy as np
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    data = []
    if len(args) == 1:
        with open(args[0]) as f:
            data = f.readlines()            
        f.close()        
        for i in range(len(data)):
            data[i] = float(data[i].replace("\n", ""))            
        print(data)
        prom = sum(data) / len(data)
        st_dev = np.std(data)
        print("El promedio es: " + str(prom) +" y la desviacion estandar es: " + str(st_dev)) ##str(round(float(st_dev),5))