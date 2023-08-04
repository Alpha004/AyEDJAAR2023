package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

// BinaryInsertionSort performs a binary insertion sort on an
// array of integers.
func BinaryInsertionSort(arr []int) []int {
	for i := 1; i < len(arr); i++ {
		currentElement := arr[i]
		pos := binaryInsertionSortSearch(arr, currentElement, 0, i)
		j := i
		for j > pos {
			arr[j] = arr[j-1]
			j--
		}
		arr[pos] = currentElement
	}
	return arr
}

// binaryInsertionSortSearch is a helper function for performing a binary search
// on the sorted part of the integer array while performing a binary insertion
// sort.
func binaryInsertionSortSearch(arr []int, item, start, end int) int {
	for start < end {
		mid := (start + end) / 2
		if arr[mid] <= item {
			start = mid + 1
			continue
		}
		end = mid
	}
	return start
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
	sorted := BinaryInsertionSort(unsorted)

	//end
	elapsed := time.Since(start).Seconds()
	log.Printf("TIME PROCESSING: %f", elapsed)
	//CREATING SORTED LIST
	fileTime, err := os.Create("BinaryInsertSortOrderedList.txt")
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
	mainpath := "../Results/Golang/binaryInsertSortResults_"
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
