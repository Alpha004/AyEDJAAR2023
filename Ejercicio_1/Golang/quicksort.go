// package main

// import (
// 	"fmt"
// 	"log"
// 	"math/big"
// 	"time"
// )

// func partition(arr []int, low, high int) ([]int, int) {
// 	pivot := arr[high]
// 	i := low
// 	for j := low; j < high; j++ {
// 		if arr[j] < pivot {
// 			arr[i], arr[j] = arr[j], arr[i]
// 			i++
// 		}
// 	}
// 	arr[i], arr[high] = arr[high], arr[i]
// 	return arr, i
// }

// func quickSort(arr []int, low, high int) []int {
// 	if low < high {
// 		var p int
// 		arr, p = partition(arr, low, high)
// 		arr = quickSort(arr, low, p-1)
// 		arr = quickSort(arr, p+1, high)
// 	}
// 	return arr
// }

// func quickSortStart(arr []int) []int {
// 	return quickSort(arr, 0, len(arr)-1)
// }

// func main() {
// 	start := time.Now()

// 	r := new(big.Int)
// 	fmt.Println(r.Binomial(1000, 10))

// 	fmt.Println(quickSortStart([]int{5, 6, 7, 2, 1, 0}))

// 	elapsed := time.Since(start)
// 	log.Printf("Binomial took %s", elapsed)
// }

package main

// QuickSort performs a quick sort on an array of
// integers.
func QuickSort(arr []int) {
	if len(arr) <= 1 {
		return
	}
	quickSortRecursive(arr, 0, len(arr)-1)
}

// quickSortRecursive is a helper function to recursively
// perform a quick sort on an array of integers.
func quickSortRecursive(arr []int, lo, hi int) {
	if lo < hi {
		p := quickSortPartition(arr, lo, hi)
		quickSortRecursive(arr, lo, p-1)
		quickSortRecursive(arr, p+1, hi)
	}
}

// quickSortPartition is a helper function to partition an
// array of integers during a quick sort and return the next
// partition index.
func quickSortPartition(arr []int, lo, hi int) int {
	pivot := arr[hi]
	i := lo
	for j := lo; j < hi; j++ {
		if arr[j] <= pivot {
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}
	arr[i], arr[hi] = arr[hi], arr[i]
	return i
}
