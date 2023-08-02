# Python program for implementation of Selection
# Sort
import sys
import time

if __name__ == '__main__':
    args = sys.argv[1:]
    lines = []
    if len(args) == 1:
        with open(args[0]) as f:
            lines = f.readlines()
            print('Cantidad de numeros en la lista: ' + str(len(lines)))
        f.close()
        start_time = time.time()
        for i in range(len(lines)):	
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i+1, len(lines)):
                if int(lines[min_idx]) > int(lines[j]):
                    min_idx = j                    
            # Swap the found minimum element with
            # the first element	
            lines[i], lines[min_idx] = lines[min_idx], lines[i]
        # Driver code to test above
        print ("Sorted array!")
        finalTime = time.time() - start_time
        print("--- TIEMPO DE PROCESAMIENTO: %s seconds ---" % finalTime)
        with open("selectionSortOrderedList.txt", "w") as txt_file:
            for line in lines:
                txt_file.write(line) # works with any number of elements in a line
        txt_file.close()        
        with open('../Results/Python/selectionSortResults_' + str(len(lines)) + '.txt', 'a') as f:
            f.write(str(finalTime) + '\n')