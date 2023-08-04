// C++ program for implementation of
// selection sort
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std::chrono;
using namespace std;

// Function for Selection sort
void selectionSort(int arr[], int n)
{
	int i, j, min_idx;

	// One by one move boundary of
	// unsorted subarray
	for (i = 0; i < n - 1; i++) {

		// Find the minimum element in
		// unsorted array
		min_idx = i;
		for (j = i + 1; j < n; j++) {
			if (arr[j] < arr[min_idx])
				min_idx = j;
		}

		// Swap the found minimum element
		// with the first element
		if (min_idx != i)
			swap(arr[min_idx], arr[i]);
	}
}

// Function to print an array
void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++) {
		cout << arr[i] << " ";
		cout << endl;
	}
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
	
	int n = sizeof(arrayNumbers) / sizeof(arrayNumbers[0]);

	// Function Call
	selectionSort(arrayNumbers, n);

	ofstream myfileRead("selectionSortOrderedList.txt");
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
    resultFile.open("../Results/C++/selectionSortResults_" + to_string(sizeNumbers) + ".txt", ios::out | ios::app);
    if (!resultFile)
    {
        ofstream fileReadTime("../Results/C++/selectionSortResults_" + to_string(sizeNumbers) + ".txt");
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

// This is code is contributed by rathbhupendra
