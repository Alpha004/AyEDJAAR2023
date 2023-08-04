// Optimized implementation of Bubble sort
#include <stdbool.h>
#include <stdio.h>
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std::chrono;
using namespace std;

void swap(int* xp, int* yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}

// An optimized version of Bubble Sort
void bubbleSort(int arr[], int n)
{
	int i, j;
	bool swapped;
	for (i = 0; i < n - 1; i++) {
		swapped = false;
		for (j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				swap(&arr[j], &arr[j + 1]);
				swapped = true;
			}
		}

		// If no two elements were swapped by inner loop,
		// then break
		if (swapped == false)
			break;
	}
}

// Driver program to test above functions
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
	bubbleSort(arrayNumbers, sizeNumbers);
	cout << "Sorted array!";
	ofstream myfileRead("bubbleSortOrderedList.txt");
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
    resultFile.open("../Results/C++/bubbleSortResults_" + to_string(sizeNumbers) + ".txt", ios::out | ios::app);
    if (!resultFile)
    {
        ofstream fileReadTime("../Results/C++/bubbleSortResults_" + to_string(sizeNumbers) + ".txt");
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
