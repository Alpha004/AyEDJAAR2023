// added by Manish Sharma
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std::chrono;
using namespace std;

int partition(int arr[], int start, int end)
{
 
    int pivot = arr[start];
 
    int count = 0;
    for (int i = start + 1; i <= end; i++) {
        if (arr[i] <= pivot)
            count++;
    }
 
    // Giving pivot element its correct position
    int pivotIndex = start + count;
    swap(arr[pivotIndex], arr[start]);
 
    // Sorting left and right parts of the pivot element
    int i = start, j = end;
 
    while (i < pivotIndex && j > pivotIndex) {
 
        while (arr[i] <= pivot) {
            i++;
        }
 
        while (arr[j] > pivot) {
            j--;
        }
 
        if (i < pivotIndex && j > pivotIndex) {
            swap(arr[i++], arr[j--]);
        }
    }
 
    return pivotIndex;
}
 
void quickSort(int arr[], int start, int end)
{
 
    // base case
    if (start >= end)
        return;
 
    // partitioning the array
    int p = partition(arr, start, end);
 
    // Sorting the left part
    quickSort(arr, start, p - 1);
 
    // Sorting the right part
    quickSort(arr, p + 1, end);
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Ha olvidado la ruta del archivo.\n");
        exit(1);
    }
    printf("Ruta %s", argv[1]);

    vector<int> numbers;
    auto startclock = high_resolution_clock::now();
    ios_base::sync_with_stdio(false);

    string line;
    ifstream myfile(argv[1]);
    if (myfile.is_open())
    {
        while (getline(myfile, line))
        {
            // cout << line << '\n';
            numbers.push_back(stoi(line));
        }
        myfile.close();
    }
    else
        cout << "Unable to open file";

    int sizeNumbers = numbers.size();
    int arrayNumbers[sizeNumbers];

    copy(numbers.begin(), numbers.end(), arrayNumbers);
	
	quickSort(arrayNumbers, 0, sizeNumbers - 1);
	
	cout << "Sorted array!";
	ofstream myfileRead("quickSortOrderedList.txt");
    if (myfileRead.is_open())
    {
        for (int i = 0; i < sizeNumbers; i++)
        {
            myfileRead << to_string(arrayNumbers[i]) + "\n";            
        }
        myfileRead.close();
    }
    else
        cout << "Unable to open file";
    // Calculating total time taken by the program.
    auto stop = high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(stop - startclock);
    printf("\nTime measured: %.9f seconds.\n", duration.count() * 1e-9);

    fstream resultFile;
    resultFile.open("../Results/C++/quickSortResults_" + to_string(sizeNumbers) + ".txt", ios::out | ios::app);
    if (!resultFile)
    {
        ofstream fileReadTime("../Results/C++/quickSortResults_" + to_string(sizeNumbers) + ".txt");
        if (fileReadTime.is_open())
        {
            fileReadTime << to_string(duration.count() * 1e-9) + "\n";
            fileReadTime.close();
        }
        else
            cout << "Unable to open file";
    }
    else
    {
        cout << "Writing\n";
        resultFile << to_string(duration.count() * 1e-9) + "\n";
    }

    return 0;
}
