// C program for implementation of
// binary insertion sort
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std::chrono;
using namespace std;
 
// A binary search based function
// to find the position
// where item should be inserted
// in a[low..high]
int binarySearch(int a[], int item,
                int low, int high)
{
    if (high <= low)
        return (item > a[low]) ?
                (low + 1) : low;
 
    int mid = (low + high) / 2;
 
    if (item == a[mid])
        return mid + 1;
 
    if (item > a[mid])
        return binarySearch(a, item,
                            mid + 1, high);
    return binarySearch(a, item, low,
                        mid - 1);
}
 
// Function to sort an array a[] of size 'n'
void insertionSort(int a[], int n)
{
    int i, loc, j, k, selected;
 
    for (i = 1; i < n; ++i)
    {
        j = i - 1;
        selected = a[i];
 
        // find location where selected should be inserted
        loc = binarySearch(a, selected, 0, j);
 
        // Move all elements after location to create space
        while (j >= loc)
        {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = selected;
    }
}
 
// Driver Code
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
 
    insertionSort(arrayNumbers, sizeNumbers);
 
    cout << "Sorted array!";
	ofstream myfileRead("binaryInsertionSortOrderedList.txt");
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
    resultFile.open("../Results/C++/binaryInsertionSortResults_" + to_string(sizeNumbers) + ".txt", ios::out | ios::app);
    if (!resultFile)
    {
        ofstream fileReadTime("../Results/C++/binaryInsertionSortResults_" + to_string(sizeNumbers) + ".txt");
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
 