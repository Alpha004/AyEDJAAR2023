package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

// SelectionSort performs a selection sort on an
// array of integers.
//
// Best Case Time Complexity: O(n^2)
// Worst Case Time Complexity: O(n^2)
func SelectionSort(arr []int) []int {
	j := 0
	arrLen := len(arr)
	for j < arrLen {
		for i := j + 1; i < arrLen; i++ {
			if arr[i] < arr[j] {
				jValue := arr[j]
				arr[j] = arr[i]
				arr[i] = jValue
			}
		}
		j++
	}
	return arr
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
	sorted := SelectionSort(unsorted)

	//end
	elapsed := time.Since(start).Seconds()
	log.Printf("TIME PROCESSING: %f", elapsed)
	//CREATING SORTED LIST
	fileTime, err := os.Create("SelectionSortOrderedList.txt")
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
	mainpath := "../Results/Golang/selectionSortResults_"
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
