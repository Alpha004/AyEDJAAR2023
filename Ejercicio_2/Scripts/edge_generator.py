import csv
import sys
import random 

CANT_EDGES_BY_V = 4

if __name__ == '__main__':
    args = sys.argv[1:]
    edge_data = []
    if len(args) == 1:
        file_graph_data = str(args[0])       
        with open(file_graph_data) as f:
            position_data = list(csv.reader(f, delimiter=" "))            
        f.close()
        #print(position_data)
        start = 1
        end = len(position_data)
        counter = 0        
        print("Generating random vertex...")
        for point in range(0,len(position_data)):
            rnd_cant_v = random.randint(0, CANT_EDGES_BY_V)
            #print("CANT DE VERTICES: " + str(rnd_cant_v))            
            for index in range(0,rnd_cant_v):
                current_point = int(position_data[point][0])
                while True:                    
                    rnd_destination = random.randint(start, end)
                    #print(rnd_destination)
                    if(rnd_destination != current_point):                                               
                        try: 
                            edge_data.index([current_point,rnd_destination])                            
                            print("DUPLICATED: " + str([current_point,rnd_destination]))
                            continue
                        except ValueError:
                            pass
                        try: 
                            edge_data.index([rnd_destination,current_point])                            
                            print("DUPLICATED: " + str([rnd_destination,current_point]))                            
                            continue
                        except ValueError:
                            pass
                        print("VALUE PASSED: " + str([current_point,rnd_destination]))
                        break                
                edge_data.append([current_point,rnd_destination])
        #print(edge_data)
            counter+=1
        with open("../Data/EDGES_" + str(end)+".txt", "w") as txt_file:
            for line in edge_data:
                txt_file.write(str(line[0]) + " " + str(line[1])+"\n") # works with any number of elements in a line
        txt_file.close()
        print("EDGES GENERATED!")
    else:
        print("Ingrese el archivo del grafico a generar posibles rutas...")