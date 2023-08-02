# Python Program implementation
# of binary insertion sort
import sys
import time

def binary_search(arr, val, start, end):
	# we need to distinguish whether we should insert
	# before or after the left boundary.
	# imagine [0] is the last step of the binary search
	# and we need to decide where to insert -1
	if start == end:
		if int(arr[start]) > int(val):
			return start
		else:
			return start+1

	# this occurs if we are moving beyond left\'s boundary
	# meaning the left boundary is the least position to
	# find a number greater than val
	if start > end:
		return start

	mid = int((start+end)/2)
	if int(arr[mid]) < int(val):
		return binary_search(arr, val, mid+1, end)
	elif int(arr[mid]) > int(val):
		return binary_search(arr, val, start, mid-1)
	else:
		return mid

def insertion_sort(arr):
	for i in range(1, len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
	return arr

# Code contributed by Mohit Gupta_OMG

if __name__ == '__main__':
    args = sys.argv[1:]
    lines = []
    if len(args) == 1:
        with open(args[0]) as f:
            lines = f.readlines()
            print('Cantidad de numeros en la lista: ' + str(len(lines)))
        f.close()
        start_time = time.time()
        lines = insertion_sort(lines)
        print ("Sorted array!")
        finalTime = time.time() - start_time
        print("--- TIEMPO DE PROCESAMIENTO: %s seconds ---" % finalTime)
        with open("BinaryInsertionSortOrderedList.txt", "w") as txt_file:
            for line in lines:
                txt_file.write(str(line)) # works with any number of elements in a line
        txt_file.close()
        with open('../Results/Python/binaryInsertionSortResults_' + str(len(lines)) + '.txt', 'a') as f:
            f.write(str(finalTime) + '\n')