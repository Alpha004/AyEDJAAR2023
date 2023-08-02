# Optimized Python program for implementation of Bubble Sort
import sys
import time

def bubblesort(arr):
	n = len(arr)
	
	# Traverse through all array elements
	for i in range(n):
		swapped = False

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# Traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if int(arr[j]) > int(arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if (swapped == False):
			break

if __name__ == '__main__':
    args = sys.argv[1:]
    lines = []
    if len(args) == 1:
        with open(args[0]) as f:
            lines = f.readlines()
            print('Cantidad de numeros en la lista: ' + str(len(lines)))
        f.close()
        start_time = time.time()
        bubblesort(lines)
        print ("Sorted array!")
        finalTime = time.time() - start_time
        print("--- TIEMPO DE PROCESAMIENTO: %s seconds ---" % finalTime)
        with open("BubbleSortOrderedList.txt", "w") as txt_file:
            for line in lines:
                txt_file.write(str(line)) # works with any number of elements in a line
        txt_file.close()
        with open('../Results/Python/bubbleSortResults_' + str(len(lines)) + '.txt', 'a') as f:
            f.write(str(finalTime) + '\n')