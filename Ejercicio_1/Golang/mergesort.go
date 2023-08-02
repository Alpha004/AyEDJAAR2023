// package main

// import (
// 	"fmt"
// 	"log"
// 	"math/big"
// 	"time"
// )

// func mergeSort(items []int) []int {
// 	if len(items) < 2 {
// 		return items
// 	}
// 	first := mergeSort(items[:len(items)/2])
// 	second := mergeSort(items[len(items)/2:])
// 	return merge(first, second)
// }

// func merge(a []int, b []int) []int {
// 	final := []int{}
// 	i := 0
// 	j := 0
// 	for i < len(a) && j < len(b) {
// 		if a[i] < b[j] {
// 			final = append(final, a[i])
// 			i++
// 		} else {
// 			final = append(final, b[j])
// 			j++
// 		}
// 	}
// 	for ; i < len(a); i++ {
// 		final = append(final, a[i])
// 	}
// 	for ; j < len(b); j++ {
// 		final = append(final, b[j])
// 	}
// 	return final
// }

// func main() {
// 	start := time.Now()

// 	r := new(big.Int)
// 	fmt.Println(r.Binomial(1000, 10))

// 	unsorted := []int{10, 6, 2, 1, 5, 8, 3, 4, 7, 9}
// 	sorted := mergeSort(unsorted)

// 	fmt.Println(sorted)

// 	elapsed := time.Since(start)
// 	log.Printf("Binomial took %s", elapsed)
// 	// sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// }

package main

// MergeSort performs a merge sort on an array of integers
// and return the sorted array.
func MergeSort(arr []int) []int {
	arrLen := len(arr)
	mid := arrLen / 2
	if arrLen <= 1 {
		return arr
	}
	a := MergeSort(arr[:mid])
	b := MergeSort(arr[mid:])
	return mergeSortMergeArray(a, b)
}

// mergeSortMergeArray is a helper function for merging/sorting
// two arrays during a merge sort.
func mergeSortMergeArray(arr1 []int, arr2 []int) []int {
	newArr := []int{}
	i := 0
	j := 0
	for i < len(arr1) && j < len(arr2) {
		if arr1[i] < arr2[j] {
			newArr = append(newArr, arr1[i])
			i++
			continue
		}
		newArr = append(newArr, arr2[j])
		j++
	}
	if i < len(arr1) {
		newArr = append(newArr, arr1[i:]...)
	}
	if j < len(arr2) {
		newArr = append(newArr, arr2[j:]...)
	}
	return newArr
}
