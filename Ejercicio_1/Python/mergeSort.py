# Python program for implementation of MergeSort
import sys
import time

def mergesort(arr):
	if len(arr) > 1:
		# Finding the mid of the array
		mid = len(arr)//2
		# Dividing the array elements
		L = arr[:mid]
		# Into 2 halves
		R = arr[mid:]
		# Sorting the first half
		mergesort(L)
		# Sorting the second half
		mergesort(R)
		i = j = k = 0
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if int(L[i]) <= int(R[j]):
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

if __name__ == '__main__':
    args = sys.argv[1:]
    lines = []
    if len(args) == 1:
        with open(args[0]) as f:
            lines = f.readlines()
            print('Cantidad de numeros en la lista: ' + str(len(lines)))
        f.close()
        start_time = time.time()
        mergesort(lines)
        print ("Sorted array!")
        finalTime = time.time() - start_time
        print("--- TIEMPO DE PROCESAMIENTO: %s seconds ---" % finalTime)
        with open("MergeSortOrderedList.txt", "w") as txt_file:
            for line in lines:
                txt_file.write(str(line)) # works with any number of elements in a line
        txt_file.close()
        with open('../Results/Python/mergeSortResults_' + str(len(lines)) + '.txt', 'a') as f:
            f.write(str(finalTime) + '\n')