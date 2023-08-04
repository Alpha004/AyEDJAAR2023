package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

func partition(arr []int, low, high int) ([]int, int) {
	pivot := arr[high]
	i := low
	for j := low; j < high; j++ {
		if arr[j] < pivot {
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}
	arr[i], arr[high] = arr[high], arr[i]
	return arr, i
}

func quickSort(arr []int, low, high int) []int {
	if low < high {
		var p int
		arr, p = partition(arr, low, high)
		arr = quickSort(arr, low, p-1)
		arr = quickSort(arr, p+1, high)
	}
	return arr
}

func quickSortStart(arr []int) []int {
	return quickSort(arr, 0, len(arr)-1)
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

	sorted := quickSortStart(unsorted)

	//end
	elapsed := time.Since(start).Seconds()
	log.Printf("TIME PROCESSING: %f", elapsed)
	//CREATING SORTED LIST
	fileTime, err := os.Create("QuickSortOrderedList.txt")
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
	mainpath := "../Results/Golang/quickSortResults_"
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
