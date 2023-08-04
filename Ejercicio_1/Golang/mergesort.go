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

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

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

func main() {
	arg := os.Args[1]
	fmt.Println(arg)
	start := time.Now()
	unsorted := []int{}
	readFile, err := os.Open(arg)
	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	for fileScanner.Scan() {
		//fmt.Println(fileScanner.Text())
		intValue := 0
		_, err := fmt.Sscan(fileScanner.Text(), &intValue)
		if err != nil {
			fmt.Println(err)
		} else {
			unsorted = append(unsorted, intValue)
		}
	}
	readFile.Close()

	//LLAMAR AL ALGORITMO

	sorted := MergeSort(unsorted)

	//end
	elapsed := time.Since(start).Seconds()
	log.Printf("TIME PROCESSING: %f", elapsed)
	//CREATING SORTED LIST
	fileTime, err := os.Create("MergeSortOrderedList.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer fileTime.Close()
	for _, line := range sorted {
		_, err := fileTime.WriteString(strconv.Itoa(line) + "\n")
		if err != nil {
			log.Fatal(err)
		}
	}
	mainpath := "../Results/Golang/bubbleSortResults_"
	//CREATING RESULTS
	// Read Write Mode

	filestatus, err := os.Stat(mainpath + strconv.Itoa(len(sorted)) + ".txt")
	if err != nil {
		fileResults, err := os.Create(mainpath + strconv.Itoa(len(sorted)) + ".txt")
		if err != nil {
			log.Fatalf("failed creating to file: %s", err)
		}
		defer fileResults.Close()
		//fileResults.WriteAt([]byte(strelapsed), 0)
		fmt.Fprintf(fileResults, "%f\n", elapsed)
		return
	}
	fmt.Println(filestatus)
	fileResults, err := os.OpenFile(mainpath+strconv.Itoa(len(sorted))+".txt", os.O_RDWR|os.O_APPEND|os.O_CREATE, 0660)
	if err != nil {
		log.Fatalf("failed opening file: %s", err)
	}
	defer fileResults.Close()
	fmt.Fprintf(fileResults, "%f\n", elapsed)
	return

}
