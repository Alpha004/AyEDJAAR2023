package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

// BubbleSort performs a bubble sort on an array of
// integers.
//
// Best Case Complexity: 	O(n)
// Average Case Complexity: O(n^2)
// Worst Case Complexity: 	O(n^2)
func BubbleSort(arr []int) []int {
	j := len(arr) - 1
	for j > 0 {
		swapped := false
		for i := 0; i < j; i++ {
			if arr[i] > arr[i+1] {
				iValue := arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = iValue
				swapped = true
			}
		}
		// if there was no swaps it means that the array
		// is already sorted.
		if !swapped {
			break
		}
		j--
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
	sorted := BubbleSort(unsorted)

	//end
	elapsed := time.Since(start).Seconds()
	log.Printf("TIME PROCESSING: %f", elapsed)
	//CREATING SORTED LIST
	fileTime, err := os.Create("BubbleSortOrderedList.txt")
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
