// C++ program for Merge Sort
// added by Manish Sharma
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std::chrono;
using namespace std;

// Merges two subarrays of array[].
// First subarray is arr[begin..mid]
// Second subarray is arr[mid+1..end]
void merge(int array[], int const left, int const mid,
		int const right)
{
	int const subArrayOne = mid - left + 1;
	int const subArrayTwo = right - mid;

	// Create temp arrays
	auto *leftArray = new int[subArrayOne],
		*rightArray = new int[subArrayTwo];

	// Copy data to temp arrays leftArray[] and rightArray[]
	for (auto i = 0; i < subArrayOne; i++)
		leftArray[i] = array[left + i];
	for (auto j = 0; j < subArrayTwo; j++)
		rightArray[j] = array[mid + 1 + j];

	auto indexOfSubArrayOne = 0, indexOfSubArrayTwo = 0;
	int indexOfMergedArray = left;

	// Merge the temp arrays back into array[left..right]
	while (indexOfSubArrayOne < subArrayOne
		&& indexOfSubArrayTwo < subArrayTwo) {
		if (leftArray[indexOfSubArrayOne]
			<= rightArray[indexOfSubArrayTwo]) {
			array[indexOfMergedArray]
				= leftArray[indexOfSubArrayOne];
			indexOfSubArrayOne++;
		}
		else {
			array[indexOfMergedArray]
				= rightArray[indexOfSubArrayTwo];
			indexOfSubArrayTwo++;
		}
		indexOfMergedArray++;
	}

	// Copy the remaining elements of
	// left[], if there are any
	while (indexOfSubArrayOne < subArrayOne) {
		array[indexOfMergedArray]
			= leftArray[indexOfSubArrayOne];
		indexOfSubArrayOne++;
		indexOfMergedArray++;
	}

	// Copy the remaining elements of
	// right[], if there are any
	while (indexOfSubArrayTwo < subArrayTwo) {
		array[indexOfMergedArray]
			= rightArray[indexOfSubArrayTwo];
		indexOfSubArrayTwo++;
		indexOfMergedArray++;
	}
	delete[] leftArray;
	delete[] rightArray;
}

// begin is for left index and end is right index
// of the sub-array of arr to be sorted
void mergeSort(int array[], int const begin, int const end)
{
	if (begin >= end)
		return;

	int mid = begin + (end - begin) / 2;
	mergeSort(array, begin, mid);
	mergeSort(array, mid + 1, end);
	merge(array, begin, mid, end);
}

// Driver code
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

	mergeSort(arrayNumbers, 0, sizeNumbers - 1);

	cout << "Sorted array!";
	ofstream myfileRead("mergeSortOrderedList.txt");
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
    resultFile.open("../Results/C++/mergeSortResults_" + to_string(sizeNumbers) + ".txt", ios::out | ios::app);
    if (!resultFile)
    {
        ofstream fileReadTime("../Results/C++/mergeSortResults_" + to_string(sizeNumbers) + ".txt");
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

// This code is contributed by Mayank Tyagi
// This code was revised by Joshua Estes
