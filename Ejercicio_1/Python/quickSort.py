# Approach 2: Quicksort using list comprehension
import sys
import time

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if int(x) < int(pivot)]
		right = [x for x in arr[1:] if int(x) >= int(pivot)]
		return quicksort(left) + [pivot] + quicksort(right)

if __name__ == '__main__':
    args = sys.argv[1:]
    lines = []
    if len(args) == 1:
        with open(args[0]) as f:
            lines = f.readlines()
            print('Cantidad de numeros en la lista: ' + str(len(lines)))
        f.close()
        start_time = time.time()
        lines = quicksort(lines)
        print ("Sorted array!")
        finalTime = time.time() - start_time
        print("--- TIEMPO DE PROCESAMIENTO: %s seconds ---" % finalTime)
        with open("QuickSortOrderedList.txt", "w") as txt_file:
            for line in lines:
                txt_file.write(str(line)) # works with any number of elements in a line
        txt_file.close()
        with open('../Results/Python/quickSortResults_' + str(len(lines)) + '.txt', 'a') as f:
            f.write(str(finalTime) + '\n')